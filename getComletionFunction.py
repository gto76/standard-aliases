#!/usr/bin/python
import sys
import re

# My take on automatic completion generation for aliases.
# Sets automoatic completion function to same function as the first command in
# alias has.
# $1 - alias
# $2 - first command of alias
#setCompletionFunctionForAlias() {
    #aliasName="$1"
    #commandName="$2"
    #completionFunction=$(complete -p "$2" 2>/dev/null)
    #if [[ "$completionFunction" == "" ]]; then
    #    return 1
    #fi  
    #completionFunction=$(
    #    echo "$completionFunction" \
    #        | cut --delimiter=' ' --fields=3)
    #complete -F "$completionFunction" "$1"
#}


#### MAIN ####

# ALIAS DEFINITION: alias wcl='wc -l'
# COMPLETION DEF:   complete -F _filedir_xspec slitex

# 1. Gets list of alias definitions as first parameter and list
# of completion functions as second.
aliases = sys.argv[1]
completions = sys.argv[2]

# 2. Returns list of completions...

#print(aliases)

import string

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
            #print("completion function: "+ completionFunction)
            print("complete -F "+completionFunction+" "+aliasName)





