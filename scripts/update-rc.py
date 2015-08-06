#!/usr/bin/python
import sys 
import re
import util
import collections

AL_FILENAME='../standard_aliases'
with open(AL_FILENAME) as f:
    aliasesContent = f.readlines()

USERS_RC_FILENAME='/home/minerva/.standard_rc'
with open(USERS_RC_FILENAME) as f:
    usersRcContent = f.readlines()

PROJECTS_RC_FILENAME='../standard_rc'
with open(PROJECTS_RC_FILENAME) as f:
    projectsRcContent = f.readlines()

RC_OPTIONS_COMMENT='./rc-options-comment'
with open(RC_OPTIONS_COMMENT) as f:
    optionsComment = f.readlines()

def getFunctions():
    functionDescriptions = []
    # go threougn aliases
    for line in aliasesContent:
        # pick up all titles
        if line.startswith("# ") and line.strip().endswith(" #"):
            functionDescriptions.append(line.strip())
        # pick up all the function names (ignore ___)
        if line.startswith("__") and not line.startswith("___"):
            line = line.strip()
            functionName = re.sub('\(.*$', '', line).strip()
            functionDescription = util.camelCaseToDescription(functionName)
            functionDescriptions.append(functionDescription)
    return functionDescriptions  

def getFunctionsWithShortcuts():
    # map: description -> shortcuts
    #shortcutsWithDescriptions = {}
    shortcutsWithDescriptions = collections.OrderedDict()
    # go trough rc
    for line in projectsRcContent:
        line = line.strip()
        # title 
        if line.startswith("# ") and line.endswith(" #"):
            shortcutsWithDescriptions[line] = ""
            continue
        # line starts with comment
        if line.startswith('#'):
            continue
        # line contains options definition
        if ";" in line:
            continue
        tokens = line.split(':')
        if len(tokens) != 2:
            continue
        shortcuts = tokens[0].strip()
        functionDescription = tokens[1].strip()
        shortcutsWithDescriptions[functionDescription] = shortcuts
    return shortcutsWithDescriptions

def getDeletedFunctions(functions, functionsWithShortcuts):
    rcFunctions = list(functionsWithShortcuts.keys())
    return list(set(rcFunctions) - set(functions))

def getDeletedBlocks(functionsWithShortcuts, deletedFunctions):
    # preceeding function -> block
    deletedBlocks = {}
    deletedBlock = ""
    lastUndeletedFunction = ""
    for function, shortcut in functionsWithShortcuts.iteritems():
        if function in deletedFunctions:
            deletedBlock += "# DELETED OR RENAMED!: "+shortcut+" : "+function+"\n"
        else:
            if deletedBlock != "":
                deletedBlocks[lastUndeletedFunction] = deletedBlock
                deletedBlock = ""
            lastUndeletedFunction = function
    return deletedBlocks

def getNewShortcutDefinitions(functions, functionsWithShortcuts, functionsWithDeletedBlock):
    rc = ""
    if "" in functionsWithDeletedBlock:
        rc += functionsWithDeletedBlock[""]+"\n"
    for function in functions:
        shortcut = functionsWithShortcuts.get(function, "")
        # title
        if function.startswith("# ") and function.endswith(" #"):
            rc += "\n"+function+"\n\n"
        else:
            rc += shortcut+" : "+function+"\n"
        if function in functionsWithDeletedBlock:
            rc += functionsWithDeletedBlock[function]
    return rc

def getOptions():
    options = ""
    for line in projectsRcContent:
        line = line.strip()
        if ";" in line:
            options += line+"\n"
    return options

def main():
    # List of function descriptions.
    functions = getFunctions()

    # Map of description -> shortcuts.
    functionsWithShortcuts = getFunctionsWithShortcuts()

    # List
    deletedFunctions = getDeletedFunctions(functions, functionsWithShortcuts)

    # Get deleted blocks in form: function -> deleted block,
    # function being the function before the deleted block
    functionsWithDeletedBlock = getDeletedBlocks(functionsWithShortcuts, deletedFunctions)

    shortcutDefs = getNewShortcutDefinitions(functions, functionsWithShortcuts, functionsWithDeletedBlock)

    # Get options
    options = getOptions()

    rc = shortcutDefs + '\n\n' + "".join(optionsComment) + '\n' + options

    print(rc)



if __name__ == '__main__':
    main()
