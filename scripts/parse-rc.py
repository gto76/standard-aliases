#!/usr/bin/python
import sys 
import re

import util
import const

aliasesContent = util.getFileContents(const.AL_FILENAME)
usersRcContent = util.getFileContents(const.USERS_RC_FILENAME)

def setCompletion(line, lastLine, currentFunction, completions, existingCompletions):
    # line tokenize form: '^' or '|' or '$('
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
    if command in completions and currentFunction:
        completions[currentFunction] = completions[command]
    elif command in existingCompletions and currentFunction:
        completions[currentFunction] = " ".join(existingCompletions[command]).strip()

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
        elif '"$@"' in line:
            setCompletion(line, lastLine, currentFunction, completions, existingCompletions)
        lastLine = intactLine
    return completions

def processOptions(tokens):
    command = tokens[0].strip()
    options = tokens[1].strip()
    if len(options) == 0:
        return
    variableName = "_"+command.upper()+"_OPTIONS"
    return "export "+variableName+"=("+options+")\n"

def processShortcut(existingCommands, completions, tokens):
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

def generateMapOfCompletions(completions):
    completionsMap = {}
    for completion in completions:
        tokens = completion.strip().split()
        completionsMap[tokens[-1]] = tokens[:-1]
    return completionsMap

def main():
    al = ""
    existingCommands = sys.argv[1].split(' ')
    existingCompletions = generateMapOfCompletions(sys.argv[2].split('\n'))
    completions = getCompletions(existingCompletions)
    modifiedCompletions = ""
    for line in usersRcContent:
        if len(line.strip()) == 0:
            continue
        if line.strip().startswith('#'):
            continue
        tokens = line.strip().split(';')
        if len(tokens) == 2:
            options = processOptions(tokens)
            if options:
                al += str(processOptions(tokens))
            continue
        tokens = line.strip().split(':')
        if len(tokens) == 2:
            al += processShortcut(existingCommands, completions, tokens)
    print(al)

if __name__ == '__main__':
    main()
