#!/usr/bin/python

# Utility functions.

from __future__ import print_function
import sys
import os
import re

# Prints passed objects to stderr.
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

# Converts passed string by uppecasing first letter.
firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''

# Converts passed string by lowercassing first letter.
firstLetterToLowercase = lambda s: s[:1].lower() + s[1:] if s else ''

# Converts description in form of a sentance (words separated 
# by spaces, ends with period) into a cammel case form.
def descriptionToCamelCase(command):
    words = []
    for word in command.split():
        words.append(firstLetterToUppercase(word))
    words[0] = firstLetterToLowercase(words[0])
    out = "".join(words)
    out = re.sub(' ', '', out)
    out = re.sub('\.', '', out)
    return "__"+out

# Converts text in form of cammel case into a sentence (First letter
# of first word in upper case, words separated by spaces, ends with period).
def camelCaseToDescription(command):
    command = command.strip('_')
    command = re.sub(r'([A-Z])',r' \1',command)
    command = command.lower()
    return firstLetterToUppercase(command)+"."

# Retruns files lines as list of strings.
def getFileContents(fileName):
    with open(fileName) as f:
        return f.readlines()


