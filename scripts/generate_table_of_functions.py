#!/usr/bin/python

# generate-table-of-functions.py
#
#

import sys 
import re

import util
import const

LENGTH_OF_CODE_SNIPPET = 15

aliasesContent = util.getFileContents(const.AL_FILENAME)
projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)
interestingContent = util.getFileContents(const.LIST_OF_IMPORTANT_FUNCTIONS)

# Gets dictionary of options from standard_rc, so they can be substitued.
# Returns:
#   * dictionary of: "${_<COMMAND-NAME>_OPTIONS[@]}" -> options.
def getOptions():
  commandsWithOptions = {}
  for line in projectsRcContent:
    if ";" in line:
      tokens = line.split(";")
      command = "\"${_"+tokens[0].strip().upper()+"_OPTIONS[@]}\""
      options = tokens[1].strip()
      commandsWithOptions[command] = options
  return commandsWithOptions

# Extracts title from the line, and adds a table header after it.
# Arguments:
#   * line - a line.
#   * heading - size of the heading.
# Returns:
#   * A heading and a table header in md format.
def getTitle(line, heading):
  ta = "\n"
  ta += heading+" "+line.strip('#').title()+"\n"
  ta += "\n"
  ta += " _Name_        | _Runs_   | _Description_  \n"
  ta += ":------------- |:--------:| ----------------\n"
  return ta

# 
# Arguments:
#   * 
# Returns:
#   * 
def getFunctionLineNumber(functionName):
  functionDefinition = functionName+"() {"
  lineStart = 0
  i = 1
  for line in aliasesContent:
    line = line.strip()
    if lineStart == 0 and functionDefinition in line:
      lineStart = i 
    elif lineStart != 0 and line == "}":
      return (lineStart, i)
    i += 1
  return (lineStart,1)

# 
# Arguments:
#   * 
# Returns:
#   * 
def getFunctionBody(lineNum, commandsWithOptions):
  i = 1
  for line in aliasesContent:
    if i == lineNum+1:
      for command, options in commandsWithOptions.iteritems():
        if command in line:
          line = line.replace(command, options)
          break
      return line.strip()[:LENGTH_OF_CODE_SNIPPET]
    i += 1
  return ""

# 
# Arguments:
#   * 
# Returns:
#   * 
def getLink(lineStart, lineEnd, pathToFunctions):
  link = pathToFunctions+"standard_functions#L"+str(lineStart)+"-L"+str(lineEnd)
  return link

# Generates tables row.
# Arguments:
#   * shortcut - short name of a function
#   * explanation - short description
#   * commandsWithOptions - body of a function
#   * pathToFunctions - relative path to standard_functions file
# Returns:
#   * example:
# **ll**       | `__listOrDisp`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L174-L175)    | List or display directory contents in pager using medium listing format. 
def getRow(shortcut, explanation, commandsWithOptions, pathToFunctions):
  # Do not print aliases that just run the command as sudo.
  if explanation.startswith("Run ") and \
    explanation.endswith(" as super user."):
    return
  functionName = util.descriptionToCamelCase(explanation)
  lineStart, lineEnd = getFunctionLineNumber(functionName)
  functionBody = getFunctionBody(lineStart, commandsWithOptions).replace('`','')
  link = getLink(lineStart, lineEnd, pathToFunctions)
  if len(functionBody) >= LENGTH_OF_CODE_SNIPPET \
    or lineEnd - lineStart > 2:
    runs = "`"+functionBody+"`[**`...`**]("+link+")"
  else:
    runs =  "`"+functionBody+"`"
  return "**"+shortcut+"** | "+runs+" | "+explanation+"\n"

# Generates tables of filtered functions.
# Returns:
#   * Tables of functions in md format.
def generateTables():
  ta = ""
  # map of: "${_COMMAND_OPTIONS[@]}" -> options
  commandsWithOptions = getOptions()
  ta += "Commands\n"
  ta += "========\n"
  for line in projectsRcContent:
    line = line.strip()
    if line.startswith('# ') and line.endswith(' #'):
      ta += getTitle(line, "###")
      continue
    if ";" in line:
      continue
    tokens = line.split(':')
    if len(tokens) == 2:
      shortcuts = tokens[0].strip()
      explanation = tokens[1].strip()
      row = getRow(shortcuts, explanation, commandsWithOptions, "../")
      ta += str(row)
  return ta

# Generates tables of all fuctions.
# Returns:
#   * Tables of functions in md format.
def main():
  ta = generateTables()
  print(ta)

if __name__ == '__main__':
  main()

