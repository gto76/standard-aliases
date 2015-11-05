#!/usr/bin/python
#
# Usage: update-readme.py
# Prints updated README.md. It substitutes tables of commands
# with newly generated ones.

import sys
import re

import util
import const

import generate_table_of_functions

TARGET_LINE = "There are currently [0-9]* commands"
TABLES_TARGET_LINE_START = "Below is a list of most useful commands."
TABLES_TARGET_LINE_END = "How To Rename Commands"

readmeContent = util.getFileContents(const.README_FILENAME)
projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)
veryInterestingFunctionsContent = util.getFileContents(const.VERY_INTERESTING_FUNCTIONS_FILENAME)

# Gets all function names that call the long function.
# Arguments:
#   * explanation - name of the long function in form of a sentence.
def getShortcuts(explanation):
  matches = [line for line in projectsRcContent if explanation in line]
  return matches[0].split(':')[0].strip()

# Generates tables of functions.
def getFunctionTables():
  ta = ""
  # map of: "${_COMMAND_OPTIONS[@]}" -> options
  commandsWithOptions = generate_table_of_functions.getOptions()
  for line in veryInterestingFunctionsContent:
    line = line.strip()
    if not line:
      continue
    if line.startswith('#'):
      ta += generate_table_of_functions.getTitle(line, "####")
      continue
    shortcuts = getShortcuts(line)
    row = generate_table_of_functions.getRow(shortcuts, line, commandsWithOptions, "")
    ta += str(row)
  return ta

# Counts number of functions defined in standard_rc.
# Returns:
#   * number of functions.
def countFunctions():
  counter = 0
  for line in projectsRcContent:
    # Counts functions (lines without ';' and with ':').
    if ';' not in line and ':' in line:
      counter += 1
  return counter

# Updates line in README.md that mentions number of functions
# with accurate number of functions and substitutes tables of
# commands.
# Arguments:
#   * noOfFunctions - no of functions.
#   * functionTables - tables of commands.
# Returns:
#   * updated README.md.
def updateReadme(noOfFunctions, functionTables):
  doPrint = True
  updatedReadme = ""
  for line in readmeContent:
    # If line contains regex.
    if re.search(TARGET_LINE, line):
      # Updates number.
      line = re.sub('[0-9]+', str(noOfFunctions), line)
    if TABLES_TARGET_LINE_START in line:
      updatedReadme += line
      updatedReadme += str(functionTables)
      doPrint = False
    if TABLES_TARGET_LINE_END in line:
      doPrint = True
      updatedReadme += '\n'
    if doPrint:
      updatedReadme += line
  return updatedReadme

def main():
  functionTables = getFunctionTables()
  noOfFunctions = countFunctions()
  updatedReadme = updateReadme(noOfFunctions, functionTables)
  print(updatedReadme)

if __name__ == '__main__':
    main()
