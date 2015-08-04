#!/usr/bin/python
from __future__ import print_function
import sys 
import re

firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''
firstLetterToLowercase = lambda s: s[:1].lower() + s[1:] if s else ''

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

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
    if tokens[0] == "sudo" or tokens[0] == "__runInBackground":
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

def getCompletions(STANDARD_ALIASES_FILENAME, existingCompletions):
    with open(STANDARD_ALIASES_FILENAME) as f:
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

# def getCompletions2(STANDARD_ALIASES_FILENAME, existingCompletions):
#     getCompletions2(STANDARD_ALIASES_FILENAME, existingCompletions)
#     completions = []
#     with open(STANDARD_ALIASES_FILENAME) as f:
#         content = f.readlines()
#     for line in content:
#         line = line.strip()
#         if line.startswith("complete "):
#             completions.append(line)
#     return completions

def glueCommand(command):
    words = []
    for word in command.split():
        words.append(firstLetterToUppercase(word))
    words[0] = firstLetterToLowercase(words[0])
    out = "".join(words)
    out = re.sub(' ', '', out)
    out = re.sub('\.', '', out)
    return out

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
        command = "__"+glueCommand(tokens[1])
        if shortcut in existingCommands or shortcut == '?':
            print("alias "+shortcut+"='"+command+"'")
            print
        else:
            print(shortcut+"() {")
            print("    "+command+" \"$@\"")
            print("}")
            if command in completions:
                print(completions[command]+" "+shortcut)
            print("# lb")

def generateMapOfCompletions(completions):
    completionsMap = {}
    for completion in completions:
        tokens = completion.strip().split()
        completionsMap[tokens[-1]] = tokens[:-1]
    return completionsMap

def main():
    RC_FILENAME = sys.argv[1]
    STANDARD_ALIASES_FILENAME = sys.argv[2]
    existingCommands = sys.argv[3].split(' ')
    existingCompletions = generateMapOfCompletions(sys.argv[4].split('\n'))
    completions = getCompletions(STANDARD_ALIASES_FILENAME, existingCompletions)
    warning(completions)
    modifiedCompletions = ""
    with open(RC_FILENAME) as f:
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
