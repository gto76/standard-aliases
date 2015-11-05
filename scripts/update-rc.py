#!/usr/bin/python
#
# Usage: update-rc.py [--user]
#
# This script updates standard_rc, by checking if there are any
# functions in standard_functions, that are not yet defined in
# standardrc, or if there are any functions that are defined in
# standardrc, but not in standard_functions.
# 
# If there is a new function it adds it to the standardrc, but
# without any alias, and if there is a function missing in
# standard_functions, then it comments it out, with a message.
#
# If there are one or more functions at the same spot, both
# missing and new, it treats them as a renamed functions, and
#
# This script takes one option: '==user', that means that users
# .standardrc should be updated instead of projects standard_rc.
# In this case the script works almost the same except for new
# functions. If new function is defined in standard_functions,
# then it first checks if there is already an alias assigned for
# it in projects standardrc. If so it then adds this definition
# to users .standardrc, but it comments it out with a message,
# so a user can decide if it wants it or not. If there is no
# definition in projects rc, then it acts same as for projects
# rc.

import sys
import os
import re
import collections

import util
import const

# Messages that are printed in front of commented out
# definitions.
DELETED_OR_RENAMED_SIGNIFIER = "# DELETED OR RENAMED FUNCTION!: "
NEW_SIGNIFIER = "# NEW FUNCTION!: "

# Lists of lines of different files.
functionsContent = util.getFileContents(const.AL_FILENAME)
usersRcContent = util.getFileContents(const.USERS_RC_FILENAME)
projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)
optionsComment = util.getFileContents(const.RC_OPTIONS_COMMENT)
usersHeader = util.getFileContents(const.USERS_RC_HEADER)
projectsHeader = util.getFileContents(const.PROJECTS_RC_HEADER)

# Returns list of all functions defined in standard_aliases,
# with names that start with two underscores (__). Names of the
# functions are converted from camelCase to sentence form.
# Returns:
#   * List of functions defined in standard_aliases.
def getFunctions():
  functionDescriptions = []
  # Goes trough aliases.
  for line in functionsContent:
    # Picks up all the titles.
    if line.startswith("# ") and line.strip().endswith(" #"):
      functionDescriptions.append(line.strip())
    # Picks up all the function names (ignores ___).
    if line.startswith("__") and not line.startswith("___"):
      line = line.strip()
      functionName = re.sub('\(.*$', '', line).strip()
      functionDescription = util.camelCaseToDescription(functionName)
      functionDescriptions.append(functionDescription)
  return functionDescriptions  

# Returns dictionary function names with alias names, as they
# are defined in passed list.
# Arguments:
#   * rcContent - list of lines from rc file (either users or
#      projects)
# Returns:
#   * Dictionary of function names with alias names.
def getFunctionsWithAliases(rcContent):
  # map: description -> aliases
  aliasesWithDescriptions = collections.OrderedDict()
  # Goes trough rc.
  for line in rcContent:
    line = line.strip()
    # Also makes use of deleted and renamed.
    if line.startswith(DELETED_OR_RENAMED_SIGNIFIER):
      line = line.replace(DELETED_OR_RENAMED_SIGNIFIER, "")
    # Title .
    if line.startswith("# ") and line.endswith(" #"):
      aliasesWithDescriptions[line] = ""
      continue
    if line.startswith('#'):
      continue
    # Line contains options definition.
    if ";" in line:
      continue
    tokens = line.split(':')
    if len(tokens) != 2:
      continue
    aliases = tokens[0].strip()
    functionDescription = tokens[1].strip()
    aliasesWithDescriptions[functionDescription] = aliases
  return aliasesWithDescriptions

# Returns list of functions that are defined in rc file, but not
# in standard_functions.
# Arguments:
#   * functions - list of functions defined in
#       standard_functions,
#   * functionsWithAliases - dictionary of functions with
#       aliases, as defined in rc file.
# Returns:
#   * List of functions that are defined in rc, but not in
#       standard_functions.
def getDeletedFunctions(functions, functionsWithAliases):
  rcFunctions = list(functionsWithAliases.keys())
  return list(set(rcFunctions) - set(functions))

# Returns a dictionary of functions with a list of functions
# that should follow the function in rc and were either deleted,
# or are new.
# Arguments:
#   * functions - list of functions either defined in
#       standard_functions, or rc file.
#   * functionsForTheBlocks - list of deleted or new functions.
# Returns:
#   * Dictionary of functions with a block that follows them.
def getBlocks(functions, functionsForTheBlocks):
  # Preceding function -> block.
  blocks = {}
  block = []
  lastFunction = ""
  for function in functions:
    if function in functionsForTheBlocks:
      block.append(function)
    else:
      if block:
        blocks[lastFunction] = block
        block = []
      lastFunction = function
  if block:
    blocks[lastFunction] = block
  return blocks

# Returns list of functions that are in first list, but not in
# second.
# Arguments:
#   * functions - list of functions,
#   * functionsWithAliases - dictionary of functions with
#       aliases.
# Returns:
#   * List of new functions.
def getNewFunctions(functions, functionsWithAliases):
  rcFunctions = list(functionsWithAliases.keys())
  return list(set(functions) - set(rcFunctions) )

# Returns list of functions that are present in both arguments.
# Arguments:
#   * functions - list of functions,
#   * functionsWithAliases - dictionary of functions with
#       aliases.
# Returns:
#   * List of unchanged functions.
def getUnchangedFunctions(functions, functionsWithAliases):
  rcFunctions = list(functionsWithAliases.keys())
  unchangedFunctions = set(functions) & set(rcFunctions)
  listOfUnchangedFunctions = []
  for function in functions:
    if function in unchangedFunctions:
      listOfUnchangedFunctions.append(function)
  return listOfUnchangedFunctions

# This function is only used when updating users rc file. It
# adds aliases that are defined in projects rc file, but not in
# users rc file to the dictionary generated from users rc. 
# Arguments:
#   * aliases - dictionary of function names with alias names,
#      that are defined in users rc.
#   * newFunctions - list of functions that are defined in
#      standard_functions but not in users rc.
def addAdditionalAliasesForUsersRc(aliases, newFunctions):
  projectsfunctionsWithAliases = \
    getFunctionsWithAliases(projectsRcContent)
  newFunctionsWithAliases = dict( \
    (newFunction, projectsfunctionsWithAliases.get(newFunction, "")) \
    for newFunction in newFunctions)
  aliases.update(newFunctionsWithAliases)

# Parses a block of functions, according to format functions.
# Arguments:
#   * block - list of functions, 
#   * aliases - dictionary of functions with aliases, 
#   * format - function that formats alias and a function into a
#      valid rc line that defines alias (like: "# NEW FUNCTION!:
#      le, less1 : Display text or file in pager.")
# Returns:
#   * Formated line that defines an alias.
def getBlockWithFormat(block, aliases, format):
  out = ""
  for function in block:
    out += format(aliases.get(function, ""), function)
  return out

# Formats an alias and a function into valid rc alias definition
# (like: "le, less1 : Display text or file in pager.").
# Arguments:
#   * alias - string with an alias name, 
#   * function - string with a function name in sentence form.
# Returns:
#   * String with alias definition.
def formatLine(alias, function):
  return alias+" : "+function+"\n"

# Formats an alias definition and prepends "# DELETED OR RENAMED
# FUNCTION!: ".
# Arguments:
#   * alias - string with an alias name, 
#   * function - string with a function name in sentence form.
# Returns:
#   * String with alias definition.
def signifyDeletedFunction(alias, function):
  return DELETED_OR_RENAMED_SIGNIFIER + formatLine(alias, function)

# Formats an alias definition and prepends "# NEW FUNCTION!: ".
# Arguments:
#   * alias - string with an alias name, 
#   * function - string with a function name in sentence form.
# Returns:
#   * String with alias definition.
def signifyNewFunction(alias, function):
  return NEW_SIGNIFIER + formatLine(alias, function)

# This function does the actual work. It iterates trough all
# functions, defined in standard_functions. If function is
# present in rc (with or without an alias), then it leaves the
# definition unchanged. If a new function is defined in
# standard_functions, then it adds an empty alias definition to
# a rc (or in case of users rc, adds it but comments it out). If
# there is a function present in rc, that is not in
# standard_functions, then it comments it out. If there is a new
# function in place of a deleted one, then it assigns an alias
# of the old function to new one (it assumes that it was
# renames).
# Arguments:
#   * unchangedFunctions - list of functions present in both
#       standard_functions and a rc file,
#   * functionsWithAliases - dictionary of function names with
#       their aliases, 
#   * functionsWithDeletedBlock - dictionary of functions with a
#       list of deleted functions that follows them,
#   * functionsWithNewBlock - dictionary of functions with a
#       list of new functions that follows them.
#   * formatDeletedFunction - function that formats a line with
#       deleted alias definition,
#   * formatNewFunction - function that formats a line with new
#       alias definition.
# Returns:
#   * Updated alias definitions.
def getNewAliasDefinitions(unchangedFunctions, \
    functionsWithAliases, \
    functionsWithDeletedBlock, \
    functionsWithNewBlock, \
    formatDeletedFunction, \
    formatNewFunction):
  rc = ""
  if "" in functionsWithDeletedBlock:
    rc += functionsWithDeletedBlock[""]+"\n"
  for function in unchangedFunctions:
    alias = functionsWithAliases.get(function, "")
    # Processes section title.
    if function.startswith("# ") and function.endswith(" #"):
      rc += "\n"+function+"\n\n"
    else:
      rc += formatLine(alias, function)
    # Checks if after current function we have both old and new
    # block of the same size.
    functionsWereRenamed = \
        function in functionsWithDeletedBlock \
      and function in functionsWithNewBlock \
      and len(functionsWithDeletedBlock[function]) == \
        len(functionsWithNewBlock[function])
    if functionsWereRenamed:
      for i in range(len(functionsWithDeletedBlock[function])):
        deletedFunction = functionsWithDeletedBlock[function][i]
        alias = functionsWithAliases.get(deletedFunction, "")
        newFunction = functionsWithNewBlock[function][i]
        rc += alias+" : "+newFunction+"\n"
    else:
      if function in functionsWithDeletedBlock:
        rc += getBlockWithFormat( \
          functionsWithDeletedBlock[function], \
          functionsWithAliases, \
          formatDeletedFunction)
      if function in functionsWithNewBlock:
        rc += getBlockWithFormat( \
          functionsWithNewBlock[function], \
          functionsWithAliases, \
          formatNewFunction)
  return rc


def getMapOfOptionsFromRc(rcContent):
  mapOfOptions = collections.OrderedDict()
  for line in rcContent:
    if ";" in line:
      tokens = line.split(';')
      commandName = "xxx"
      if len(tokens) >= 1:
        commandName = tokens[0].strip()
      options = "yyy"
      if len(tokens) >= 2:
        options = tokens[1].strip()
      mapOfOptions[commandName] = options
  return mapOfOptions

def getCommandsWithOptionVariables():
  setOfOptionVariables = util.OrderedSet()
  for match in re.findall("_([A-Z_]+)_OPTIONS", "\n".join(functionsContent)):
    commandName = util.underscoreToCamelcase(match)
    setOfOptionVariables.add(commandName)
  return  setOfOptionVariables

def getOptions(rcContent):
  mapOfOptions = getMapOfOptionsFromRc(rcContent)
  commandsWithOptionVariables = getCommandsWithOptionVariables()
  out = ""
  for command in commandsWithOptionVariables:
    # assemble options conf line
    options = mapOfOptions.get(command, "")
    out += command + " ; " + options + "\n"
  return out

# Extracts options definition from a list of lines of a rc file.
# (for example: "ls ; --classify -X -C --color=auto
# --group-directories-first")
# Arguments:
#   * rcContent - list of lines of rc file.
# Returns:
#   * List of lines that define options variables.
def getOptionsOLD(rcContent):
  options = ""
  for line in rcContent:
    line = line.strip()
    if ";" in line:
      options += line+"\n"
  return options


# Prints updated passed rc file. 
# Arguments:
#   * rcContent - list of lines of rc file,
#   * addAdditionalAliases - function that takes dictionary of
#       functions with aliases and a list of functions and in case
#       of users rc updates the dictionary with new functions and
#       their aliases.  In case of projects rc, function doesn't do
#       anything.
#   * formatDeletedFunction - function that formats a line with
#       alias definition, and prepends a comment that tells the
#       function was deleted. It takes two strings, first one is a
#       list of aliases and second one a function name in form of a
#       sentence
#   * formatNewFunction - same, but prepends message that a
#       function is new in case of users rc, and in case of projects
#       rc, just processes the line normally.
#   * header - string with header that is attached at a
#       beginning of rc file.
# Returns:
#   * Prints the processed rc file.
def generateRc(rcContent, addAdditionalAliases, \
    formatDeletedFunction, formatNewFunction, header):
  rc = "".join(header)+"\n\n"
  # List of function descriptions.
  functions = getFunctions()
  # Map of description -> aliases.
  functionsWithAliases = getFunctionsWithAliases(rcContent)
  # List of deleted functions.
  deletedFunctions = \
    getDeletedFunctions(functions, functionsWithAliases)
  # Gets deleted blocks in form of function -> deleted block,
  # where function is a function before the deleted block.
  functionsWithDeletedBlock = \
    getBlocks(functionsWithAliases.keys(), deletedFunctions)
  newFunctions = \
    getNewFunctions(functions, functionsWithAliases)
  functionsWithNewBlock = \
    getBlocks(functions, newFunctions)
  unchangedFunctions = \
    getUnchangedFunctions(functions, functionsWithAliases)
  # Adds aliases of new functions from the projects rc if
  # processing users rc.
  addAdditionalAliases(functionsWithAliases, newFunctions)
  newAliasDefs = \
    getNewAliasDefinitions(unchangedFunctions, functionsWithAliases, \
      functionsWithDeletedBlock, functionsWithNewBlock, \
      formatDeletedFunction, formatNewFunction)
  options = getOptions(rcContent)
  rc += newAliasDefs + '\n\n' + "".join(optionsComment) + '\n' + options
  print(rc)

# Prints updated standard_rc.
def generateProjectsRc():
  generateRc(projectsRcContent, lambda x, y: None, \
    signifyDeletedFunction, formatLine, projectsHeader)

# Prints updated ~/.standardrc.
def generateUsersRc():
  generateRc(usersRcContent, addAdditionalAliasesForUsersRc, \
    signifyDeletedFunction, signifyNewFunction, usersHeader)

# Prints updated standard_rc or ~/.standardrc, depending on
# first argument.
# Arguments:
#   * sys.argv[1]: string '--user' - optional. If passed then
#      processes users ~/.standardrc file instead of projects
#      standard_rc.
# Returns:
#   * Prints updated rc file.
def main():
  userOprionPresent = len(sys.argv) == 2 and sys.argv[1] == '--user'
  if userOprionPresent:
    generateUsersRc()
  else:
    generateProjectsRc()

if __name__ == '__main__':
  main()
