#!/usr/bin/python
import re

STANDARD_ALIASES_FILENAME = "/home/minerva/github/standard-aliases/standard_aliases"
CONF_FILENAME = "/home/minerva/github/standard-aliases/confTemp"
ALIASES_FILENAME = "/home/minerva/github/standard-aliases/aliasesTemp"

confFile = [] 
confSection = []

standardAliases = []

with open(STANDARD_ALIASES_FILENAME) as f:
    content = f.readlines()

title = False
lastAlias = ""

firstLetterToUppercase = lambda s: s[:1].upper() + s[1:] if s else ''

def processAliases(sameAliases, lastFunction):
    sameAliases = list(reversed(sameAliases))
    commaSeparatedAliases = ",".join(sameAliases)
    return commaSeparatedAliases+":"+lastFunction


def combineAliases(confSection):
    aliasesOut = []
    lastFunction = ""
    sameAliases = []
    for line1 in confSection:
        #print("line is "+ line1)
        tokens = line1.split(':')
        alias = tokens[0]
        #print("alias is "+ alias)
        function = tokens[1]
        #print("function is "+ function)
        # if new function and last function is not ""
        if function != lastFunction and lastFunction != "":
            processedLine = processAliases(sameAliases, lastFunction)
            aliasesOut.append(processedLine)
            sameAliases = []
        # add alias to same aliases
        sameAliases.append(alias)
        # save function into last function
        lastFunction = function
    # save sameAliases and last Function
    processedLine = processAliases(sameAliases, lastFunction)
    aliasesOut.append(processedLine)
    return aliasesOut 


# Iterate over lines.
for line in content:
    line = line.strip('\n')
    if line.startswith("# ") and title:
        confFile.append(line)
        standardAliases.append(line)
        continue
    # If line starts with '######' then print this and next two
    # lines to both files.
    if line.startswith("######") and title:
        title = False
        confFile.append(line)
        standardAliases.append(line)
        continue
    if line.startswith("######"):
        title = True
        confFile.append("")
        confSection = combineAliases(confSection)
        confFile.extend(confSection)
        confFile.append("")
        confSection = []
        confFile.append(line)
        standardAliases.append(line)
        continue
    # If line starts with alias.  
    if line.startswith("alias"):
        # Convert and print to confFile, but check if next alias
        # has same function, in that case separate alias names
        # with comma and then print function name.
        tokens = line.split()
        tokens2 = tokens[1].split('=')
        aliasName = tokens2[0]
        alias = tokens2[1].strip('\'')
        alias = alias.strip('__')
        alias = re.sub(r'([A-Z])',r' \1',alias)
        alias = alias.lower()
        alias = firstLetterToUppercase(alias)
        confSection.append(aliasName+" : "+alias+".")
        continue
    # Else print to standard Aliases.
    standardAliases.append(line)

# Save to file
with open(CONF_FILENAME, 'w') as f:
    for item in confFile:
        f.write(item+"\n")

# Save to file
with open(ALIASES_FILENAME, 'w') as f:
    for item in standardAliases:
        f.write(item+"\n")

