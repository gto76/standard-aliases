#!/usr/bin/python
#
# Usage: remove-conflicts-from-rc.py
#
# Prints projects configuration file with commands that are
# already defined as aliases (in .bashrc, .profile, ...)
# commented out.

import sys
import re
import commands

import util
import const

projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)

def main():
  conflicts = set(commands.getstatusoutput('./get-conflicting-names')[1].split('\n'))
  print(conflicts)
  for line in projectsRcContent:
    line = line.strip()
    lineIsAComment = line.startswith('#')
    if lineIsAComment:
      print(line)
      continue
    lineDefinesOptions = ";" in line
    if lineDefinesOptions:
      print(line)
      continue
    tokens = line.split(':')
    lineIsNotComplete = len(tokens) != 2
    if lineIsNotComplete:
      print(line)
      continue
    aliases = tokens[0].strip().split(',')
    for alias in aliases:
      alias.strip()
    intersection = conflicts.intersection(aliases)
    if not intersection:
      print(line)
      continue
    print("# NAME "+intersection.pop()+" ALREADY TAKEN BY AN ALIAS: "+line)

if __name__ == '__main__':
  main()
