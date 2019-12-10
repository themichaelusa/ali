"""
*  ali/utilities.py
*
*  Utilities 
*
*  Copyright (C) 2019 Michael Usachenko
*
*  This file is subject to the terms and conditions of the GNU General Public
*  License Version 3. See the file LICENSE in the main directory of the ali repository
*  for more details.
"""

### IMPORTS
import os
import shutil
import subprocess

import ali
import constants as const

### GENERAL FUNCS

get_shell_type = lambda: os.getenv('SHELL').rstrip().split('/')[-1]

# design question... do we cache this once? or get it each time?
# only gets default shell, not CURRENT shell... something to figure out
get_rc_file_type = lambda: const.SHELL_TYPE_TO_RC_DICT[get_shell_type()]

def dotrc_file_as_dict():

    mod_dict = {}
    with open(os.path.expanduser(get_rc_file_type()), 'r') as rc_file:
        all_aliases = (alias.split('\n')[0] for alias in rc_file.readlines())
        all_aliases = (tuple(alias.split('=')) for alias in all_aliases)

        for alias_name_raw, alias_cmd in all_aliases:
            alias_name = alias_name_raw.split(' ')[1]
            mod_dict[alias_name] = alias_cmd
    
        mod_dict = {k:v.replace('"', '') for k,v in mod_dict.items()}

    return mod_dict

# question: is write on python buffered?
def save_dotrc_file(mod_dict):
    with open(os.path.expanduser(get_rc_file_type()), 'w') as rc_file:
        for name, cmd in mod_dict.items():
            rc_file.write(const.ALIAS_STR.format(name, cmd))
        rc_file.flush()

### DEBUG 
def uninstall_ali():

    # remove key aliases
    ali.remove('areload')
    ali.remove('ali')

    # remove ali folder 
    shutil.rmtree(const.ALI_DIR_LOC)

if __name__ == '__main__':
   print(get_shell_type())

