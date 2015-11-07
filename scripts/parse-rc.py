#!/usr/bin/python
#
# Usage: parse-rc.py ALL-EXISTING-COMMANDS ALL-EXISTING-COMPLETIONS 
#
# This script parses ~/.standardrc, and prints result to stdout.
# Output should then be saved to file named
# ~/.standars_aliases/aliases, that gets loaded by .bashrc every
# time a new Bash shell is run.
#
# This script expects two arguments:
#   sys.argv[1] - containing all existing commands, and
#   sys.argv[2] - containing all existing completions.
#
# ~/.standardrc is a configuration file that defines shorter
# function names and options. For example, if line in standardrc
# looks like this:
#   le, less1 : Display text or file in pager.
# then this script interprets it as:
#   le() {
#       __displayTextOrFileInPager "$@" 
#   }
#   less1() {
#       __displayTextOrFileInPager "$@" 
#   }
#
# And if line with options definition looks like this:
#   ls ; --classify -X -C --color=auto --group-directories-first
# then this script interprets it as:
#   export _LS_OPTIONS=(--classify -X -C --color=auto
#      --group-directories-first)
#
# Besides interpreting short function names and options, this
# script also checks if any of the called functions (right side
# of the colon) has a defined completion in standard_functions.
# If so it defines same completion for the function with shorter
# name. If the function doesn't have a completion defined, then
# it checks the completion of the function inside that function
# that gets called with "$@" (all command arguments).
#
# If the short name is already taken, then it's defined as an
# alias instead of a function.

import sys 
import re

import util
import const

# Lists of lines of different files.
aliasesContent = util.getFileContents(const.AL_FILENAME)
usersRcContent = util.getFileContents(const.USERS_RC_FILENAME)
aliasesHeader = util.getFileContents(const.ALIASES_HEADER)

# Converts list of completion definitions into a dictionary that
# maps a command to its completion.
# Arguments:
#   * completions - list of completions ("complete -F _longopt
#       cat", ...) of all commands.
# Returns: 
#   * Dictionary of: command -> completion ("cat" -> "complete
#       -F _longopt", ...) of all available commands.
def generateMapOfCompletions(completions):
  completionsMap = {}
  if not completions:
    return completionsMap
  for completion in completions:
    tokens = completion.strip().split()
    completionsMap[tokens[-1]] = tokens[:-1]
  return completionsMap

# Finds out which command/function on the line is called with
# "$@" and returns its completion.
# Arguments:
#   * line - line containing "$@",
#   * lastLIne - line before that, in case of options and
#       command being on separate lines,
#   * completions - dictionary of: function -> completion, that
#       contains completions of the functions that were found so
#       far and
#   * existingCompletions - dictionary of: command -> completion
#       of all available commands.
# Returns:
#   * String with completion in form of: "complete -F _longopt".
def deduceCompletion(line, lastLine, completions, existingCompletions):
  # Tokenizes line from '^' or '|' or '$(' to "$@".
  line = re.sub('"\$@".*$',"",line.strip())
  line = re.sub('^.*\|',"",line.strip())
  line = re.sub('^.*\$\(',"",line.strip())
  optionsAreOnOwnLine = line.startswith('-')
  if optionsAreOnOwnLine:
    line = lastLine.strip()[:-1]
  tokens = line.split()
  if not tokens:
    return
  if tokens[0] == "sudo" or tokens[0] == "__runCommandInBackground":
    if len(tokens) < 2:
      return
    command = tokens[1]
  else:
    command = tokens[0]
  if command == "apt-get" or command == "git":
    return
  if command in completions:
    return completions[command]
  elif command in existingCompletions:
    return " ".join(existingCompletions[command]).strip()

# Generates dictionary of functions defined in
# standard_functions, with their completion function. It does
# that by searching standard_functions for completion
# definitions and if function lacks one, then it tries to deduct
# one, by examining which function does the function call with
# all arguments ("$@").
# Arguments:
#   * existingCompletions - dictionary of: command -> completion
#       ("cat" -> "complete -F _longopt", ...) of all available
#       commands.
# Returns:
#   * dictionary of: command -> completion ("ll" -> "complete -F
#       _longopt", ...) of functions defined in standard_functions.
def getCompletions(existingCompletions):
  completions = {}
  currentFunction = ""
  lastLine = ""
  for intactLine in aliasesContent:
    line = intactLine
    if line.startswith("complete "):
      tokens = line.strip().split()
      function = tokens[-1]
      completion = " ".join(tokens[:-1])
      completions[function] = completion
    elif line.startswith("__"):
      currentFunction = line.split()[0].strip('()')
    elif line.startswith("}"):
      currentFunction = ""
    elif '"$@"' in line and currentFunction:
      completion = deduceCompletion(line, lastLine, completions, 
                                    existingCompletions)
      if completion:
        completions[currentFunction] = completion
    lastLine = intactLine
  return completions

# Interprets line that defines commands options as an assignment
# of that options to bash array (see files comment for details).
# Arguments:
#   * tokens - list with two strings, first one is part of the
#       line before semicolon (;), and second one the part after
#       it.
# Returns:
#   * String that assigns options to a bash array.
def processOptions(tokens):
  command = tokens[0].strip()
  options = tokens[1].strip()
  if len(options) == 0:
    return ""
  variableName = "_"+util.camelcaseToUnderscore(command).upper()+"_OPTIONS"
  return "export "+variableName+"=("+options+")\n"

# Interprets line that defines alias as one function for each
# alias (see files comment for details).
# Arguments:
#   * existingCommands - list of existing commands,
#   * completions - dictionary of function names and their
#       completions
#   * tokens - list of two strings, first one containing
#       aliases, separated by commas, and second one containing a
#       function name (in form of sentence).
# Returns:
#   * String with functions.
def processAlias(existingCommands, completions, tokens):
  fun = ""
  shortcuts = tokens[0]
  shortcutTokens = shortcuts.split(',')
  for shortcut in shortcutTokens:
    shortcut = shortcut.strip()
    command = util.descriptionToCamelCase(tokens[1])
    if not shortcut:
      continue
    if shortcut in existingCommands or shortcut == '?':
      fun += "alias "+shortcut+"='"+command+"'\n\n"
    else:
      fun += shortcut+"() {\n"
      fun += "    "+command+" \"$@\"\n"
      fun += "}\n"
      if command in completions:
        fun += completions[command]+" "+shortcut+"\n"
      fun += "\n"
  return fun

def main():
  al = "".join(aliasesHeader)+"\n"
  existingCommands = sys.argv[1].split(' ')
  existingCompletions = \
      generateMapOfCompletions(sys.argv[2].split('\n'))
  completions = getCompletions(existingCompletions)
  modifiedCompletions = ""
  for line in usersRcContent:
    if len(line.strip()) == 0:
      continue
    if line.strip().startswith('#'):
      continue
    tokens = line.strip().split(';')
    if len(tokens) == 2:
      al += processOptions(tokens)
      continue
    tokens = line.strip().split(':')
    if len(tokens) == 2:
      al += processAlias(existingCommands, completions, tokens)
  print(al)

if __name__ == '__main__':
  main()
