#!/usr/bin/python

import sys 
import re

import util
import const

LENGTH_OF_CODE_SNIPPET = 15

aliasesContent = util.getFileContents(const.AL_FILENAME)
projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)
interestingContent = util.getFileContents(const.LIST_OF_IMPORTANT_FUNCTIONS)

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
def getLink(lineStart, lineEnd):
    link = "https://github.com/gto76/standard-aliases/blob/master/functions#L"+str(lineStart)+"-L"+str(lineEnd)
    return link

# 
# Arguments:
#   * 
# Returns:
#   * 
# **ll**       | `__listOrDisp`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L174-L175)    | List or display directory contents in pager using medium listing format. 
def getRow(shortcut, explanation, commandsWithOptions):
    # Do not print aliases that just run the command as sudo.
    if explanation.startswith("Run ") and \
        explanation.endswith(" as super user."):
        return
    functionName = util.descriptionToCamelCase(explanation)
    lineStart, lineEnd = getFunctionLineNumber(functionName)
    functionBody = getFunctionBody(lineStart, commandsWithOptions).replace('`','')
    link = getLink(lineStart, lineEnd)
    if len(functionBody) >= LENGTH_OF_CODE_SNIPPET \
        or lineEnd - lineStart > 2:
        runs = "`"+functionBody+"`[**`...`**]("+link+")"
    else:
        runs =  "`"+functionBody+"`"
    return "**"+shortcut+"** | "+runs+" | "+explanation+"\n"

# 
# Arguments:
#   * 
# Returns:
#   * 
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
def getOptions():
    # map of: "${_COMMAND_OPTIONS[@]}" -> options
    commandsWithOptions = {}
    for line in projectsRcContent:
        if ";" in line:
            tokens = line.split(";")
            command = "\"${_"+tokens[0].strip().upper()+"_OPTIONS[@]}\""
            options = tokens[1].strip()
            commandsWithOptions[command] = options
    return commandsWithOptions

# 
# Arguments:
#   * 
# Returns:
#   * 
def generateTable(filter):
    ta = ""
    # map of: "${_COMMAND_OPTIONS[@]}" -> options
    commandsWithOptions = getOptions()
    ta += "Commands\n"
    if filter:
        ta += "--------\n"    
    else:
        ta += "========\n"
    for line in projectsRcContent:
        line = line.strip()
        if line.startswith('# ') and line.endswith(' #'):
            if filter and line not in filter:
                continue
            if filter:
                ta += getTitle(line, "####")
            else:
                ta += getTitle(line, "###")
            continue
        if ";" in line:
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            shortcut = tokens[0].strip()
            explanation = tokens[1].strip()
            if filter and explanation not in filter:
                continue
            row = getRow(shortcut, explanation, commandsWithOptions)
            ta += str(row)
    return ta

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '--readme':
        stripped = [line.strip() for line in interestingContent]
        ta = generateTable(stripped)
    else:
        ta = generateTable([])
    print(ta)

if __name__ == '__main__':
    main()

