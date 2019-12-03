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

def setup():

	subprocess.call(['mkdir', const.ALI_DIR_LOC], shell=True)
	subprocess.call(['chmod', '755', const.ALI_DIR_LOC], shell=True)

	# get abs path of fresh ali directory
	ali_path = os.path.dirname(os.path.abspath(__file__))

	# get paths of all files in ali directory
	all_file_paths = list(glob.glob(ali_path + "**/*", recursive=True))

	# copies over all files 
	for file in all_file_paths:
		subprocess.call(['sudo', 'cp', file, const.ALI_DIR_LOC])
		new_path = '{}/{}'.format(const.ALI_DIR_LOC, file)
		subprocess.call(['chmod', '755', new_path], shell=True)

	# drop setup files 
	subprocess.call(['rm', '{}/ali_setup.py'.format(const.ALI_DIR_LOC)])


if __name__ == '__main__':
	setup()

