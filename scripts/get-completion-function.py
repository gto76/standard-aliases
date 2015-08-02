#!/usr/bin/python
import sys
import re
import string

#### MAIN ####

# ALIAS DEFINITION: alias wcl='wc -l'
# COMPLETION DEF:   complete -F _filedir_xspec slitex

# 1. Gets list of alias definitions as first parameter and list
# of completion functions as second.
aliases = sys.argv[1]
completions = sys.argv[2]

# 2. Returns list of completions...
out = ""

for alias in string.split(aliases, '\n'):
    aliasName = re.sub(r'^alias ', "", alias) 
    aliasName = re.sub(r'=.*', "", aliasName) 
    commandName = re.sub(r'^.*?\'', "", alias) 
    commandName = re.sub(r' .*', "", commandName) 
    commandName = re.sub(r'\'', "", commandName) 
    #print
    #print("aliasName: " + aliasName)
    #print("commandName: " + commandName)
    for completion in completions.split("\n"):
        if completion.endswith(" "+commandName):
            parts = completion.strip().split(' ')
            completionFunction= parts[2]
            out += "complete -F "+completionFunction+" "+aliasName+"\n"

print(out)





