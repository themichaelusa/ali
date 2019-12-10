"""
*  ali/constants.py
*
*  Constant vars used by ali and it's subsystems.
*
*  Copyright (C) 2019 Michael Usachenko
*
*  This file is subject to the terms and conditions of the GNU General Public
*  License Version 3. See the file LICENSE in the main directory of the ali repository
*  for more details.
"""

import utilities as utils

# SETUP
ALI_DIR_LOC = '/usr/local/lib/ali'
RM_SETUP_FILE = ['rm', '{}/ali_setup.py'.format(ALI_DIR_LOC)]
ALI_ALIAS_SETUP = ['python3', 'ali.py', 'add', 'ali', 'python3 {}/ali.py'.format(ALI_DIR_LOC)]

# again, this may be an achilles heel? tied to one shell at a time? export options later?
ARELOAD_ALIAS_SETUP = ['python3', 'ali.py', 'add', 'areload', 'exec {}'.format(utils.get_shell_type())]

# SHELL TYPES
# TODO: add ksh, csh, fish
SHELL_TYPE_TO_RC_DICT = {
'sh': '~/.shrc',
'zsh': '~/.zshrc',
'bash': '~/.bashrc',
}

GET_SHELL_TYPE_SCRIPT = './get_shell_type.sh'

# ALI COMMANDS
CMD_SHOW = ''
CMD_ADD = 'add'
CMD_REMOVE = 'remove'
CMD_RENAME = 'rename'
CMD_REUSE = 'reuse'

# ALIAS UTILS
ALIAS_STR = 'alias {}="{}"\n'

# DISPLAY 
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

HEADER_STR = color.BOLD + "{:<12} {:<20}".format('Alias','Command') + color.END
