SHELL := /bin/bash

all: standard_rc ~/.standardrc ~/.standard_aliases/aliases doc/FUNCTION_DESCRIPTIONS.md README.md

# Projects configuration file (only used on install). Gets
# updated if there are any new/deleted/renamed functions in
# standard_functions.
standard_rc: standard_functions scripts/update-rc.py scripts/util.py scripts/const.py scripts/resources/rc-options-comment
	temp=$(shell mktemp XXXXXXXX); \
	./scripts/update-rc.py > "$$temp"; \
	cp "$$temp" standard_rc

# Users configuration file. Gets updated if there are any
# new/deleted/renamed functions in standard_functions (update is
# more nondestructive than for projects rc file).
~/.standardrc: standard_functions standard_rc scripts/update-rc.py scripts/util.py scripts/const.py scripts/resources/rc-options-comment
	temp=$(shell mktemp XXXXXXXX); \
	./scripts/update-rc.py --user > "$$temp"; \
	cp "$$temp" ~/.standardrc

# Automatically generated file containing functions with short
# names (as defined in users configuration file) that call
# functions with longer names (located in standard_functions).
# It also assigns appropriate command-line completions to the
# short functions and exports variables that contain command
# options (as defined in users configuration file).
~/.standard_aliases/aliases: standard_functions ~/.standardrc scripts/generate-aliases scripts/parse-rc.py scripts/util.py scripts/const.py
	./scripts/generate-aliases > ~/.standard_aliases/aliases

# Markdown file with tables that describe all commands.
doc/FUNCTION_DESCRIPTIONS.md: standard_rc standard_functions scripts/generate_table_of_functions.py scripts/util.py scripts/const.py
	./scripts/generate_table_of_functions.py > doc/FUNCTION_DESCRIPTIONS.md

# Readme.
README.md: standard_rc scripts/update-readme.py scripts/generate_table_of_functions.py
	temp=$(shell mktemp XXXXXXXX); \
	./scripts/update-readme.py > "$$temp"; \
	cp "$$temp" README.md

