#!/usr/bin/env python3

# Utility functions.

import sys
import os
import re

# Prints passed objects to stderr.
def warning(*objs):
  print("WARNING: ", *objs, file=sys.stderr)

# Converts passed string by uppercasing first letter.
firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''

# Converts passed string by lowercasing first letter.
firstLetterToLowercase = lambda s: s[:1].lower() + s[1:] if s else ''

# Converts description in form of a sentence (words separated by
# spaces, ends with period) into a camel case form.
def descriptionToCamelCase(command):
  words = []
  for word in command.split():
    words.append(firstLetterToUppercase(word))
  words[0] = firstLetterToLowercase(words[0])
  out = "".join(words)
  out = re.sub(' ', '', out)
  out = re.sub('\.', '', out)
  return "__"+out

# Converts text in form of camel case into a sentence (First
# letter of first word in upper case, words separated by spaces,
# ends with period).
def camelCaseToDescription(command):
  command = command.strip('_')
  command = re.sub(r'([A-Z])',r' \1',command)
  command = command.lower()
  return firstLetterToUppercase(command)+"."

# Retruns files lines as list of strings.
def getFileContents(fileName):
  with open(fileName) as f:
    return f.readlines()

def underscoreToCamelcase(command):
  out = ""
  command = command.strip('_')
  command = command.strip(' ')
  tokens = command.split('_')
  first = True
  for token in tokens:
    token = token.lower()
    if not first:
      token = firstLetterToUppercase(token)
    out += token
    first = False
  return out

def camelcaseToUnderscore(command):
  command = command.strip(' ')
  s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', command)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

from collections.abc import MutableSet

class OrderedSet(MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

