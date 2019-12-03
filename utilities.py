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
import subprocess
import constants as const

def get_rc_file_type():

	#  supports: sh, bash, zsh | to support: ksh, csh, fish, etc 
	#  only gets default shell, not CURRENT shell... something to figure out

    # get shell type 
    ps_out = subprocess.check_output([const.GET_SHELL_TYPE_SCRIPT], shell=True)
    #ps_out = subprocess.check_output(['echo', '"$SHELL"'], shell=True)
    shell_type_raw = ps_out.decode('utf8').rstrip()
    shell_type = shell_type_raw.split('/')[-1]

    # resolve rc file type
    return const.SHELL_TYPE_TO_RC_DICT[shell_type]

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

if __name__ == '__main__':
    print(get_rc_file_type())
