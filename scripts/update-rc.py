#!/usr/bin/python
import sys
import os
import re
import collections

import util
import const

DELETED_OR_RENAMED_SIGNIFIER = "# DELETED OR RENAMED FUNCTION!: "
NEW_SIGNIFIER = "# NEW FUNCTION!: "

aliasesContent = util.getFileContentsRelative(const.AL_FILENAME)
usersRcContent = util.getFileContents(const.USERS_RC_FILENAME)
projectsRcContent = util.getFileContentsRelative(const.PROJECTS_RC_FILENAME)
optionsComment = util.getFileContentsRelative(const.RC_OPTIONS_COMMENT)

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

def getFunctionsWithShortcuts(rcContent):
    # map: description -> shortcuts
    shortcutsWithDescriptions = collections.OrderedDict()
    # go trough rc
    for line in rcContent:
        line = line.strip()
        # also make use of deleted and renamed
        if line.startswith(DELETED_OR_RENAMED_SIGNIFIER):
            line = line.replace(DELETED_OR_RENAMED_SIGNIFIER, "")
        # title 
        if line.startswith("# ") and line.endswith(" #"):
            shortcutsWithDescriptions[line] = ""
            continue
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
    deletedBlock = []
    lastUndeletedFunction = ""
    for function, shortcut in functionsWithShortcuts.iteritems():
        if function in deletedFunctions:
            deletedBlock.append(function)
        else:
            if deletedBlock:
                deletedBlocks[lastUndeletedFunction] = deletedBlock
                deletedBlock = []
            lastUndeletedFunction = function
    return deletedBlocks

def getNewFunctions(functions, functionsWithShortcuts):
    rcFunctions = list(functionsWithShortcuts.keys())
    return list(set(functions) - set(rcFunctions) )

def getNewBlocks(functions, newFunctions):
    # preceeding function -> block
    newBlocks = {}
    newBlock = []
    lastUndeletedFunction = ""
    for function in functions:
        if function in newFunctions:
            newBlock.append(function)
        else:
            if newBlock:
                newBlocks[lastOldFunction] = newBlock
                newBlock = []
            lastOldFunction = function
    return newBlocks

def getUnchangedFunctions(functions, functionsWithShortcuts):
    rcFunctions = list(functionsWithShortcuts.keys())
    unchangedFunctions = set(functions) & set(rcFunctions)
    listOfUnchangedFunctions = []
    for function in functions:
        if function in unchangedFunctions:
            listOfUnchangedFunctions.append(function)
    return listOfUnchangedFunctions

def formatLine(shortcut, function):
    return shortcut+" : "+function+"\n"

def signifyDeletedFunction(shortcut, function):
    return DELETED_OR_RENAMED_SIGNIFIER + formatLine(shortcut, function)

def signifyNewFunction(shortcut, function):
    return NEW_SIGNIFIER + formatLine(shortcut, function)

def getBlockWithFormat(block, shortcuts, format):
    out = ""
    for function in block:
        out += format(shortcuts.get(function, ""), function)
    return out

def getNewShortcutDefinitions(functions, \
        functionsWithShortcuts, \
        functionsWithDeletedBlock, \
        functionsWithNewBlock, \
        formatDeletedFunction, \
        formatNewFunction):
    rc = ""
    if "" in functionsWithDeletedBlock:
        rc += functionsWithDeletedBlock[""]+"\n"
    for function in functions:
        shortcut = functionsWithShortcuts.get(function, "")
        # title
        if function.startswith("# ") and function.endswith(" #"):
            rc += "\n"+function+"\n\n"
        else:
            rc += formatLine(shortcut, function)
        # check if after this functions we have both old and new block and if they are both of size 1
        functionsWereRenamed = function in functionsWithDeletedBlock \
            and function in functionsWithNewBlock \
            and len(functionsWithDeletedBlock[function]) == len(functionsWithNewBlock[function])
        if functionsWereRenamed:
            for i in range(len(functionsWithDeletedBlock[function])):
                shortcut = functionsWithShortcuts.get(functionsWithDeletedBlock[function][i], "")
                blockFunction = functionsWithNewBlock[function][i]
                rc += shortcut+" : "+blockFunction+"\n"
        else:
            if function in functionsWithDeletedBlock:
                rc += getBlockWithFormat(functionsWithDeletedBlock[function], \
                    functionsWithShortcuts, \
                    formatDeletedFunction)
            if function in functionsWithNewBlock:
                rc += getBlockWithFormat(functionsWithNewBlock[function], \
                    functionsWithShortcuts, \
                    formatNewFunction)
    return rc

def getOptions(rcContent):
    options = ""
    for line in rcContent:
        line = line.strip()
        if ";" in line:
            options += line+"\n"
    return options

def generateProjectsRc():
    # List of function descriptions.
    functions = getFunctions()
    # Map of description -> shortcuts.
    functionsWithShortcuts = getFunctionsWithShortcuts(projectsRcContent)
    # List
    deletedFunctions = \
        getDeletedFunctions(functions, functionsWithShortcuts)
    # Get deleted blocks in form: function -> deleted block,
    # function being the function before the deleted block
    functionsWithDeletedBlock = \
        getDeletedBlocks(functionsWithShortcuts, deletedFunctions)
    newFunctions = \
        getNewFunctions(functions, functionsWithShortcuts)
    functionsWithNewBlock = \
        getNewBlocks(functions, newFunctions)
    unchangedFunctions = getUnchangedFunctions(functions, functionsWithShortcuts)
    newShortcutDefs = \
        getNewShortcutDefinitions(unchangedFunctions, functionsWithShortcuts, \
            functionsWithDeletedBlock, functionsWithNewBlock, \
            signifyDeletedFunction, formatLine)
    # Get options
    options = getOptions(projectsRcContent)
    rc = newShortcutDefs + '\n\n' + "".join(optionsComment) + '\n' + options
    print(rc)


def generateUsersRc():
    # List of function descriptions.
    functions = getFunctions()
    # Map of description -> shortcuts.
    functionsWithShortcuts = getFunctionsWithShortcuts(usersRcContent) # DIFF
    # List
    deletedFunctions = \
        getDeletedFunctions(functions, functionsWithShortcuts)
    # Get deleted blocks in form: function -> deleted block,
    # function being the function before the deleted block
    functionsWithDeletedBlock = \
        getDeletedBlocks(functionsWithShortcuts, deletedFunctions)
    newFunctions = \
        getNewFunctions(functions, functionsWithShortcuts)
    functionsWithNewBlock = \
        getNewBlocks(functions, newFunctions)
    unchangedFunctions = getUnchangedFunctions(functions, functionsWithShortcuts)
    # DIFF > TODO : check tha one that are already new
    # add shortcuts of new functions from projects rc
    projectsfunctionsWithShortcuts = getFunctionsWithShortcuts(projectsRcContent)
    newFunctionsWithShortcuts = dict( \
        (newFunction, projectsfunctionsWithShortcuts.get(newFunction, "")) \
        for newFunction in newFunctions)
    functionsWithShortcuts.update(newFunctionsWithShortcuts)
    # > DIFF
    newShortcutDefs = \
        getNewShortcutDefinitions(unchangedFunctions, functionsWithShortcuts, \
            functionsWithDeletedBlock, functionsWithNewBlock, \
            signifyDeletedFunction, signifyNewFunction) # DIFF
    # Get options
    options = getOptions(usersRcContent) # DIFF todo
    rc = newShortcutDefs + '\n\n' + "".join(optionsComment) + '\n' + options
    print(rc)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '--user':
        generateUsersRc()
    else:
        generateProjectsRc()

if __name__ == '__main__':
    main()
