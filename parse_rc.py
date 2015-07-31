#!/usr/bin/python
import sys 
import re

RC_FILENAME = "/home/minerva/.standardrc"
STANDARD_ALIASES_FILENAME = "/home/minerva/.standard_aliases"


def getCompletions():
    completions = []
    with open(STANDARD_ALIASES_FILENAME) as f:
        content = f.readlines()
    for line in content:
        line = line.strip()
        if line.startswith("complete "):
            completions.append(line)
    return completions


def glueCommand(command):
    return re.sub(' ', '', command)

def main():
    completions = getCompletions()
    modifiedCompletions = ""
    with open(RC_FILENAME) as f:
        content = f.readlines()
    for line in content:
        tokens = line.strip().split(':')
        if len(tokens) != 2:
            continue 
        shortcut = tokens[0]
        command = "__"+glueCommand(tokens[1])
        print(shortcut+"() {")
        print("    "+command+" \"$@\"")
        print("}")
        completion = [i for i in completions if i.endswith(command)][0]
        if len(completion) != 0:
            print(re.sub(command, shortcut, completion))
        print

if __name__ == '__main__':
    main()
