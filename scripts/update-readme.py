#!/usr/bin/python
import sys
import re

import util
import const

import generate_table_of_functions

TARGET_LINE = "There are currently [0-9]* commands"
TABLES_TARGET_LINE_START = "Below is a list of most useful commands."
TABLES_TARGET_LINE_END = "How It Works"

readmeContent = util.getFileContents(const.README_FILENAME)
projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)
veryInterestingFunctionsContent = util.getFileContents(const.VERY_INTERESTING_FUNCTIONS_FILENAME)

def getShortcuts(explanation):
  matches = [line for line in projectsRcContent if explanation in line]
  return matches[0].split(':')[0].strip()

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
# * number of functions.
def countFunctions():
  counter = 0
  for line in projectsRcContent:
    # Counts functions (lines withouth ';' and with ':').
    if ';' not in line and ':' in line:
      counter += 1
  return counter

# Updates line in README.md that mentiones number of functions with acurate number of functions.
# Arguments:
#   * noOfFunctions - no of functions.
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
