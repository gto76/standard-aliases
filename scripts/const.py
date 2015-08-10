import os
from os.path import expanduser

homeDir = expanduser("~")
scriptsDir = os.path.dirname(__file__)

USERS_RC_FILENAME = os.path.join(homeDir, '.standardrc')
AL_FILENAME = os.path.join(scriptsDir, '../standard_functions')
PROJECTS_RC_FILENAME = os.path.join(scriptsDir, '../standard_rc')
RC_OPTIONS_COMMENT = os.path.join(scriptsDir, 'resources/rc-options-comment')
LIST_OF_IMPORTANT_FUNCTIONS = os.path.join(scriptsDir, '../doc/interesting-functions')