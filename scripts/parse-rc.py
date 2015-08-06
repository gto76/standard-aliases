#!/usr/bin/python
import sys 
import re

import util
import const

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
    with open(const.AL_FILENAME) as f:
        content = f.readlines()
    completions = {}
    currentFunction = ""
    lastLine = ""
    for intactLine in content:
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
    print("export "+variableName+"=("+options+")")

def processShortcut(existingCommands, completions, tokens):
    shortcuts = tokens[0]
    shortcutTokens = shortcuts.split(',')
    for shortcut in shortcutTokens:
        shortcut = shortcut.strip()
        command = util.descriptionToCamelCase(tokens[1])
        if shortcut in existingCommands or shortcut == '?':
            print("alias "+shortcut+"='"+command+"'")
            print
        else:
            print(shortcut+"() {")
            print("    "+command+" \"$@\"")
            print("}")
            if command in completions:
                print(completions[command]+" "+shortcut)
            print("")

def generateMapOfCompletions(completions):
    completionsMap = {}
    for completion in completions:
        tokens = completion.strip().split()
        completionsMap[tokens[-1]] = tokens[:-1]
    return completionsMap

def main():
    existingCommands = sys.argv[1].split(' ')
    existingCompletions = generateMapOfCompletions(sys.argv[2].split('\n'))
    completions = getCompletions(existingCompletions)
    modifiedCompletions = ""
    with open(const.USERS_RC_FILENAME) as f:
        content = f.readlines()
    for line in content:
        if len(line.strip()) == 0:
            continue
        if line.strip().startswith('#'):
            continue
        tokens = line.strip().split(';')
        if len(tokens) == 2:
            processOptions(tokens)
            continue
        tokens = line.strip().split(':')
        if len(tokens) == 2:
            processShortcut(existingCommands, completions, tokens)

if __name__ == '__main__':
    main()
