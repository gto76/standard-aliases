#!/usr/bin/python
#
# Usage: remove-conflicts-from-rc.py
#
# Prints modified projects configuration file, so it is ready to
# be copied into users home directory as users config file.  It
# changes its header and comments out the commands that are
# already defined as aliases (in .bashrc, .profile, ...).

import sys
import re
import commands

import util
import const

projectsRcContent = util.getFileContents(const.PROJECTS_RC_FILENAME)
usersHeader = util.getFileContents(const.USERS_RC_HEADER)

def main():
  conflicts = set(commands.getstatusoutput('./get-conflicting-names')[1].split('\n'))
  header = True
  for line in projectsRcContent:
    line = line.strip()
    if line == "# LESS #":
      header = False
      print(''.join(usersHeader))
      print('')
    if header:
      continue
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
