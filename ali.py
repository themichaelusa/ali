"""
*  ali/ali.py
*
*  Entrypoint + Main Logic for the ali CLI tool.
*
*  Copyright (C) 2019 Michael Usachenko
*
*  This file is subject to the terms and conditions of the GNU General Public
*  License Version 3. See the file LICENSE in the main directory of the ali repository
*  for more details.
"""

"""
features in the works:
-  ali (just shows ali header, list of all aliases)
-  ali reload
-  ali add <name> <cmd>
-  ali remove <name>
-  ali rename <curr_name> <new_name>
-  ali reuse <name> <new_cmd>
-  ali <name> dynamic search with tab
-  on dynamic search: show options tab below

long term --> online sharing of aliases/shell scripts:
- ali install <package name>
- ali remove <package name>
- ali register <package name>
"""

### IMPORTS
import os
import sys
import subprocess

import constants as const
import utilities as utils

def show():
    alias_dict = utils.dotrc_file_as_dict()
    alias_dict.pop('ali')
    alias_dict.pop('areload')

    print("{:<12} {:<20}".format('Alias','Command'))
    for alias, cmd in alias_dict.items():
        print("{:<12} {:<20}".format(alias, cmd))

def add(name, cmd):
    mod_dict = utils.dotrc_file_as_dict()
    mod_dict[name] = cmd
    utils.save_dotrc_file(mod_dict)

def remove(name):
    mod_dict = utils.dotrc_file_as_dict()
    result = mod_dict.get(name, None)

    if result is None:
        # TODO: Throw snarky error message
        pass
    else:
        removed_cmd = mod_dict.pop(name)
        # TODO: throw message say successfully removed

    utils.save_dotrc_file(mod_dict)

def rename(old_name, new_name):
    mod_dict = utils.dotrc_file_as_dict()
    result = mod_dict.get(old_name, None)

    if result is None:
        # TODO: Throw snarky error message
        pass
    else:
        mod_dict[new_name] = mod_dict[old_name]
        removed_cmd = mod_dict.pop(old_name)
        # TODO: throw message say successfully removed

    utils.save_dotrc_file(mod_dict)

def reuse(name, new_cmd):
    mod_dict = utils.dotrc_file_as_dict()
    result = mod_dict.get(name, None)

    if result is None:
        # TODO: Throw snarky error message
        pass
    else:
        mod_dict[name] = new_cmd
        # TODO: throw message say successfully changed

    utils.save_dotrc_file(mod_dict)

def ali():

    args = sys.argv

    if len(args)-1 == 0:
        show()
        return

    command = args[1]
    if command == const.CMD_REMOVE:
        remove(args[2])
    elif command == const.CMD_ADD:
        add(args[2], ' '.join(args[3:]))
    elif command == const.CMD_RENAME:
        rename(args[2], args[3:4])
    elif command == const.CMD_REUSE:
        reuse(args[2], args[3:])

if __name__ == '__main__':
    ali()
