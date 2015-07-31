
STANDARD_ALIASES_FILENAME = "standard_aliases"
CONF_FILENAME = "confTemp"
ALIASES_FILENAME = "aliasesTemp"

confFile = ""
standardAliases = ""

with open(STANDARD_ALIASES_FILENAME) as f:
    content = f.readlines()

title = False
lastAlias = ""

# Iterate over lines.
for line in content:
    # Strip line.
    line = line.strip()
    if title:
        confFile.append(line)
        standardAliases.append(line)
        title = False
    # If line starts with '######' then print this and next two
    # lines to both files.
    if line.startswith("######"):
        confFile.append(line)
        standardAliases.append(line)
        title = True
    # If line is empty continue.
    if len(line) == 0:
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
        confFile.append(aliasName+" : "+alias)
    # Else print to standard Aliases.
    standardAliases.append(line)

# Save to file
with open(CONF_FILENAME) as f:
    for item in confFile:
        f.write(item)

# Save to file
with open(ALIASES_FILENAME) as f:
    for item in standardAliases:
        f.write(item)

