#!/usr/bin/python
from __future__ import print_function
import sys
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


