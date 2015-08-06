#!/usr/bin/python
import sys 
import re
import util

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

def getFunctionBody(lineNum):
    i = 1
    for line in aliasesContent:
        if i == lineNum+1:
            return line.strip()[:10]
        i += 1
    return ""

def getLink(lineStart, lineEnd):
    link = "https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L"+str(lineStart)+"-L"+str(lineEnd)
    return link

# **ll**       | `__listOrDisp`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L174-L175)    | List or display directory contents in pager using medium listing format. 
def processRow(tokens):
    name = tokens[0].strip()
    explanation = tokens[1].strip()
    functionName = util.descriptionToCamelCase(explanation)
    lineStart, lineEnd = getFunctionLineNumber(functionName)
    functionBody = getFunctionBody(lineStart)
    link = getLink(lineStart, lineEnd)
    print("**"+name+"** | `"+functionBody+"`[**`...`**]("+link+") | "+explanation)

def main():
    scriptsDir = sys.argv[1]
    openFiles(scriptsDir)
    print("Commands")
    print("========")
    for line in projectsRcContent:
        line = line.strip()
        if line.startswith('# ') and line.endswith(' #'):
            print("")
            print("## "+line.strip('#').title())
            print("")
            print(" _Name_        | _Runs_   | _Description_  ")
            print(":------------- |:--------:| ----------------")
        if ";" in line:
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            processRow(tokens)

if __name__ == '__main__':
    main()
