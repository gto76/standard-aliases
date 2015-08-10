#!/usr/bin/python
from __future__ import print_function
import sys
import os
import re

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''
firstLetterToLowercase = lambda s: s[:1].lower() + s[1:] if s else ''

def descriptionToCamelCase(command):
    words = []
    for word in command.split():
        words.append(firstLetterToUppercase(word))
    words[0] = firstLetterToLowercase(words[0])
    out = "".join(words)
    out = re.sub(' ', '', out)
    out = re.sub('\.', '', out)
    return "__"+out

def camelCaseToDescription(command):
    command = command.strip('_')
    command = re.sub(r'([A-Z])',r' \1',command)
    command = command.lower()
    return firstLetterToUppercase(command)+"."

def getFileContents(fileName):
    with open(fileName) as f:
        return f.readlines()

# def getFileContentsRelative(fileName):
#     path = os.path.dirname(__file__)
#     fileName = os.path.join(path, fileName)
#     with open(fileName) as f:
#         return f.readlines()


