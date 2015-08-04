#!/usr/bin/python
import sys 
import re


def getFunctionName(explanation):
	return "bla"

def getFunctionBody(functionName):
	return "bla"

def getLink(functionName):
	return "bla"


# **ll**       | `__listOrDisp`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L174-L175)    | List or display directory contents in pager using medium listing format. 
def processRow(tokens):
	name = tokens[0]
	explanation = tokens[1]
	functionName = getFunctionName(explanation)
	functionBody = getFunctionBody(functionName)
	link = getLink(functionName)
	print("**"+name+"** | `"+functionBody+"`[**`...`**]("+link+") | "+explanation)

def main():
    RC_FILENAME='../standard_rc'
    with open(RC_FILENAME) as f:
        content = f.readlines()
    for line in content:
        if line.strip().startswith('#'):
            print("")
            print("##"+line)
            print("_Name_        | _Runs_  | _Description_  ")
            print(":------------- |:--------:| --------")
        tokens = line.strip().split(':')
        if len(tokens) == 2:
            processRow(tokens)

if __name__ == '__main__':
    main()
