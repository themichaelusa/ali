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
	subprocess.call(['rm', '{}/ali_setup.py'.format(const.ALI_DIR_LOC)])

if __name__ == '__main__':
	setup()

