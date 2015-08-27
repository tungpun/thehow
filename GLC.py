#!/usr/bin/python2.7

def config_bashrc():
	# TODO
	print '[+]', 'File .bashrc was updated ! Thehow saved the backup to .bashrc.bak'
	return 0


def get_zsh_last_command():
	# TODO	
	return "cat main.py"


def get_bash_last_command():
	# TODO
	return 0


def get_shell():
	# TODO
	# return 'zsh', 'bash'.. or 0
	return 'zsh' # for testing


def get_last_command():
	config_bashrc()
	shell = get_shell()

	if shell == 'bash':
		return get_bash_last_command()
	elif shell == 'zsh':
		return get_zsh_last_command()
	else:
		raise Exception, "Shell not found"

	return 0


def get_prefix(command):
	try:
		prefix = command.split(' ')[0]
	except Exception, e:
		print e
		raise Exception, "Get prefix: error ! Let me check your last command !"
	return prefix


if __name__ == '__main__':
	"""
	For testing
	"""
	print get_last_command()
	