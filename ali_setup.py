"""
*  ali/ali_setup.py
*
*  Setup Logic for the ali CLI tool.
*
*  Copyright (C) 2019 Michael Usachenko
*
*  This file is subject to the terms and conditions of the GNU General Public
*  License Version 3. See the file LICENSE in the main directory of the ali repository
*  for more details.
"""

### IMPORTS
import os
import glob
import subprocess
import constants as const
import utilities as utils

def manual_setup(debug=False):

	if debug is True:
		utils.uninstall_ali()

	# init ali dir in /usr/local/lib
	os.mkdir(const.ALI_DIR_LOC)

	# get abs path of fresh ali directory
	ali_path = os.path.dirname(os.path.abspath(__file__))

	# get paths of all files in ali directory
	all_file_paths = list(glob.glob(ali_path + "**/*", recursive=True))

	# copies over all files 
	for file in all_file_paths:
		subprocess.call(['cp', file, const.ALI_DIR_LOC])
		file_name = file.split('/')[-1]
		new_path = '{}/{}'.format(const.ALI_DIR_LOC, file_name)

		try:
			subprocess.check_output(['chmod', '777', new_path])
		except subprocess.CalledProcessError:
			pass # nothing required... for pycache error 

	# drop setup files 
	subprocess.call(const.RM_SETUP_FILE)

	# set up "ali" and "areload" alias
	subprocess.call(const.ALI_ALIAS_SETUP)
	subprocess.call(const.ARELOAD_ALIAS_SETUP)

	# ask user politely to type "areload"
	print('Please type "areload" to start using ali!')

if __name__ == '__main__':
	manual_setup(debug=True)

