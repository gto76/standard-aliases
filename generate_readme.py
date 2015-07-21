#!/usr/bin/python
import sys
import re

# Loads file in list of strings.
with open("standard_aliases") as f:
    content = f.readlines()

def getIndexOfFirstCommentedLineBefore(i):
    while i > 0:
        line = content[i]
        if line.startswith('#'):
            return i
        i -= 1
    return 0

def getIndexOfLastCommentedLineBefore(i):
    while i > 0:
        line = content[i]
        if not line.startswith('#'):
            return i + 1
        i -= 1
    return 0

# Returns string containing comment for alias that is defined at
# line number 'i'. If there is no one line above the alias, it
# then searches backwards util it finds the first comment on the
# first column. This is useful for aliases that only give a
# different name for function defined directly above them.
def getCommentForLine(i):
    commentEnd = getIndexOfFirstCommentedLineBefore(i)
    commentStart = getIndexOfLastCommentedLineBefore(commentEnd)
    # print "commentStart", commentStart
    # print "commentEnd", commentEnd
    out = ""
    for i in range(commentStart, commentEnd+1):
        lineWithRemovedComment = re.sub(r'^# *', "", content[i])
        out += lineWithRemovedComment
    return out

##### MAIN #####

for i in range(len(content)):
    line = content[i]
    # Line contains title of the section.
    if line.startswith('######') and content[i+2].startswith('######'):
        title = re.sub(r'#', "", content[i+1])
        title = re.sub(r' ', "", title)
        print("### " + title)
    # Line contains definition of an alias.
    if line.startswith('alias'):
        name = re.sub(r'alias ', "", line)        
        name = re.sub(r'=.*', "", name)        
        name = re.sub(r'\n', "", name)        
        comment = getCommentForLine(i)
        print(name + " - " + comment)

