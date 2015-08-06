#!/usr/bin/python
import sys 
import re
import util

LENGTH_OF_CODE_SNIPPET = 20

AL_FILENAME = '../standard_aliases'
PROJECTS_RC_FILENAME = '../standard_rc'

aliasesContent = ""
projectsRcContent = ""

def openFiles(scriptsDir):
    global aliasesContent, projectsRcContent
    if not scriptsDir.endswith('/'):
        scriptsDir = scriptsDir+'/'
    with open(scriptsDir + PROJECTS_RC_FILENAME) as f:
        projectsRcContent = f.readlines()
    with open(scriptsDir + AL_FILENAME) as f:
        aliasesContent = f.readlines()

def getFunctionLineNumber(functionName):
    functionDefinition = functionName+"() {"
    lineStart = 0
    i = 1
    for line in aliasesContent:
        line = line.strip()
        if lineStart == 0 and functionDefinition in line:
            lineStart = i
        elif lineStart != 0 and "}" in line:
            return (lineStart, i)
        i += 1
    return (lineStart,1)

def getFunctionBody(lineNum, commandsWithOptions):
    i = 1
    for line in aliasesContent:
        if i == lineNum+1:
            for command, options in commandsWithOptions.iteritems():
                if command in line:
                    print("#################################")
                    line = line.replace(command, options)
                    break
            return line.strip()[:LENGTH_OF_CODE_SNIPPET]
        i += 1
    return ""

def getLink(lineStart, lineEnd):
    link = "https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L"+str(lineStart)+"-L"+str(lineEnd)
    return link

# **ll**       | `__listOrDisp`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L174-L175)    | List or display directory contents in pager using medium listing format. 
def processRow(tokens, commandsWithOptions):
    name = tokens[0].strip()
    explanation = tokens[1].strip()
    # Do not print aliases that just run the command as sudo.
    if explanation.startswith("Run ") and \
        explanation.endswith(" as super user."):
        return
    functionName = util.descriptionToCamelCase(explanation)
    lineStart, lineEnd = getFunctionLineNumber(functionName)
    functionBody = getFunctionBody(lineStart, commandsWithOptions)
    link = getLink(lineStart, lineEnd)
    print("**"+name+"** | `"+functionBody+"`[**`...`**]("+link+") | "+explanation)

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

def main():
    scriptsDir = sys.argv[1]
    openFiles(scriptsDir)
    # map of: "${_COMMAND_OPTIONS[@]}" -> options
    commandsWithOptions = getOptions()
    print("Commands")
    print("========")
    for line in projectsRcContent:
        line = line.strip()
        if line.startswith('# ') and line.endswith(' #'):
            print("")
            print("### "+line.strip('#').title())
            print("")
            print(" _Name_        | _Runs_   | _Description_  ")
            print(":------------- |:--------:| ----------------")
        if ";" in line:
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            processRow(tokens, commandsWithOptions)
    print(commandsWithOptions)

if __name__ == '__main__':
    main()
