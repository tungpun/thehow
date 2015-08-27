#!/usr/bin/python2.7
import os


def config_bashrc():
    import shutil
    shutil.copy2(os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.bashrc.bak"))
    f = open(os.path.expanduser("~/.bashrc"), "a")
    f.write('PROMPT_COMMAND="history -a;$PROMPT_COMMAND"')
    print '[+]', 'File .bashrc was updated ! Thehow saved the backup to .bashrc.bak'


def get_zsh_last_command():
    with open(os.path.expanduser("~/.zsh_history")) as f:
        list_commands = f.readlines()
    last_command = list_commands[-1].split(';')[1]
    return last_command


def get_bash_last_command():
    with open(os.path.expanduser("~/.bash_history")) as f:
        list_commands = f.readlines()
    last_command = list_commands[-1]
    return last_command


def get_shell():
    environ = os.environ["SHELL"]
    shell = environ.split('/')[2]
    return shell


def get_last_command():
    shell = get_shell()

    if shell == 'bash':
        config_bashrc()
        return get_bash_last_command()
    elif shell == 'zsh':
        return get_zsh_last_command()
    else:
        raise Exception, "Shell not found"


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
