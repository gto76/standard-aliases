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


def getCompletions2(STANDARD_ALIASES_FILENAME):
    with open(STANDARD_ALIASES_FILENAME) as f:
        content = f.readlines()
    # map command > completion
    completions = {}
    currentFunction = ""
    # read line by line
    for line in content:
        # if "complete" > map
        if line.startswith("complete "):
            tokens = line.strip().split()
            function = tokens[-1]
            completion = " ".join(tokens[:-1])
            completions[function] = completion
            continue
        # if function name > function
        if line.startswith("__"):
            currentFunction = line.split()[0].strip('()')
            continue
        # if } erase function
        if line.startswith("}"):
            currentFunction = ""
            continue
        # if "$@"
        if '"$@"' in line:
            # line tokenize form ^ or |
            line = re.sub('"$@".*$',"",line.strip())
            line = re.sub('^.*|',"",line.strip())
            tokens = line.split()
            if token[0] == "sudo" or token[0] == "__runInBackground":
                command = token[1]
            else:
                command = token[0]
            if command == "apt-get" or command == "git":
                continue
            if command in completions and currentFunction:
                completions[currentFunction] = completions[command]
            # if command in map
                # complete command
            # if command apt-get or git continue
            # map command = completion command
    # return completions

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
