#!/usr/bin/python2.7 
#
#		  __  .__           .__                   
#		_/  |_|  |__   ____ |  |__   ______  _  __
#		\   __\  |  \_/ __ \|  |  \ /  _ \ \/ \/ /
#		 |  | |   Y  \  ___/|   Y  (  <_> )     / 
#		 |__| |___|  /\___  >___|  /\____/ \/\_/  
#		           \/     \/     \/               v0.0
#											
#			       			Help you view help command
#


import GLC
import os
import subprocess as sub

KNOWN_PREFIX = ['cd', 'ls', 'clear']			# Two examples
POSTFIX = ['-h', '--help']


def known_prefix(prefix):
	os.system('man ' + prefix)	
	return 0 


def run(command):	
	p = sub.Popen(command,stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
	output, errors = p.communicate()
	return output


def is_verified(stdout):
	if 'invalid' in stdout:
		return False
	return True


def unknown_prefix(prefix):	
	os.system(prefix + ' --help')	
	return 0	

	# print "[+]", "Not found help command for", prefix	


if __name__ == '__main__':			
	command = GLC.get_last_command()			# echo Example
	prefix = GLC.get_prefix(command).strip()	# echo		
	if prefix in KNOWN_PREFIX:
		known_prefix(prefix)
	else:
		unknown_prefix(prefix)