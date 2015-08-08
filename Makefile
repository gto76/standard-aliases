SHELL := /bin/bash

all: standardrc ~/.standardrc ~/.standard_aliases/shortcuts FUNCTION_DESCRIPTIONS.md doc/SHORTER_FUNCTION_DESCRIPTIONS.md

standardrc: functions scripts/update-rc.py scripts/util.py scripts/const.py scripts/resources/rc-options-comment
	temp=$(shell tempfile); \
	./scripts/update-rc.py > "$$temp"; \
	cp "$$temp" standardrc

~/.standardrc: functions standardrc scripts/update-rc.py scripts/util.py scripts/const.py scripts/resources/rc-options-comment
	temp=$(shell tempfile); \
	./scripts/update-rc.py --user > "$$temp"; \
	cp "$$temp" ~/.standardrc

~/.standard_aliases/shortcuts: functions ~/.standardrc scripts/generate-shortcuts scripts/parse-rc.py scripts/util.py scripts/const.py
	./scripts/generate-shortcuts

FUNCTION_DESCRIPTIONS.md: standardrc functions scripts/generate-table-for-readme.py scripts/util.py scripts/const.py
	./scripts/generate-table-for-readme.py > FUNCTION_DESCRIPTIONS.md

doc/SHORTER_FUNCTION_DESCRIPTIONS.md: standardrc functions scripts/generate-table-for-readme.py scripts/util.py scripts/const.py doc/interesting-functions
	./scripts/generate-table-for-readme.py --readme > doc/SHORTER_FUNCTION_DESCRIPTIONS.md