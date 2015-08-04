#!/usr/bin/python
import sys 
import re

firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''
firstLetterToLowercase = lambda s: s[:1].lower() + s[1:] if s else ''

AL_FILENAME='../standard_aliases'
with open(AL_FILENAME) as f:
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

def descriptionToCamelCase(command):
    words = []
    for word in command.split():
        words.append(firstLetterToUppercase(word))
    words[0] = firstLetterToLowercase(words[0])
    out = "".join(words)
    out = re.sub(' ', '', out)
    out = re.sub('\.', '', out)
    return "__"+out

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
    functionName = descriptionToCamelCase(explanation)
    lineStart, lineEnd = getFunctionLineNumber(functionName)
    functionBody = getFunctionBody(lineStart)
    link = getLink(lineStart, lineEnd)
    print("**"+name+"** | `"+functionBody+"`[**`...`**]("+link+") | "+explanation)

def main():
    RC_FILENAME='../standard_rc'
    with open(RC_FILENAME) as f:
        content = f.readlines()
    for line in content:
        line = line.strip()
        if line.startswith('# ') and line.endswith(' #'):
            print("")
            print("### "+line.strip('#').title())
            print("")
            print(" _Name_        | _Runs_   | _Description_  ")
            print(":------------- |:--------:| ----------------")
        tokens = line.split(':')
        if len(tokens) == 2:
            processRow(tokens)

if __name__ == '__main__':
    main()
