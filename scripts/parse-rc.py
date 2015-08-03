#!/usr/bin/python
import sys 
import re

#RC_FILENAME = "/home/minerva/.standardrc"
#STANDARD_ALIASES_FILENAME = "/home/minerva/.standard_aliases"

firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''
firstLetterToLowercase = lambda s: s[:1].lower() + s[1:] if s else ''

def getCompletions(STANDARD_ALIASES_FILENAME):
    completions = []
    with open(STANDARD_ALIASES_FILENAME) as f:
        content = f.readlines()
    for line in content:
        line = line.strip()
        if line.startswith("complete "):
            completions.append(line)
    return completions

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
            completion = [i for i in completions if i.endswith(command)]
            if len(completion) != 0:
                print(re.sub(command, shortcut, completion[0]))
            print

def main():
    RC_FILENAME = sys.argv[1]
    STANDARD_ALIASES_FILENAME = sys.argv[2]
    existingCommands = sys.argv[3].split(' ')
    completions = getCompletions(STANDARD_ALIASES_FILENAME)
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
