#!/usr/bin/python
import sys
import re

import util
import const

TARGET_LINE = "There are [0-9]* functions"

readmeContent = util.getFileContents(const.README_FILENAME)
projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)

# Counts number of functions defined in standard_rc.
# Returns:
#	* number of functions.
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
def updateReadme(noOfFunctions):
	updatedReadme = ""
	for line in readmeContent:
		# If line contains regex.
		if re.search(TARGET_LINE, line):
			# Updates number.
			line = re.sub('[0-9]+', str(noOfFunctions), line)
		updatedReadme += line
	return updatedReadme

def main():
	noOfFunctions = countFunctions()
	updatedReadme = updateReadme(noOfFunctions)
	print(updatedReadme)

if __name__ == '__main__':
    main()
