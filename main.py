import GLC

KNOWN_PREFIX = ['git', 'nmap']			# Two examples
POSTFIX = ['-h', '--help']


def known_prefix(prefix):
	# TODO
	return 0 


def run(command):
	# TODO
	# return stdout
	return 0


def is_verified(stdout):
	# TODO
	return False


def unknown_prefix(prefix):
	# TODO
	for postfix in POSTFIX:
		helpcommand = prefix + ' ' + postfix
		stdout = run(helpcommand)
		if is_verified(stdout):
			print stdout
			return 0
	print "[+]", "Not found help command for", prefix
	return 0


if __name__ == '__main__':
	command = GLC.get_last_command()	# echo Example
	prefix = GLC.get_prefix(command)	# echo	
	if prefix in KNOWN_PREFIX:
		known_prefix(prefix)
	else:
		unknown_prefix(prefix)
