#!/usr/bin/python2.7
import os
import shutil


def config_bashrc():
    try:
        shutil.copy2(os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.bashrc.bak"))
        f = open(os.path.expanduser("~/.bashrc"), "r+a")
        lines = f.readlines()
        command = 'PROMPT_COMMAND="history -a;$PROMPT_COMMAND"'
        if command not in lines:
            f.write(command)
            print '[+]', 'File .bashrc was updated ! Thehow saved the backup to .bashrc.bak'
        f.close()
    except Exception, e:
        print e
        raise Exception, "Config .bashrc file! Error when write file"


def get_zsh_last_command():
    try:
        with open(os.path.expanduser("~/.zsh_history"), "r") as f:
            list_commands = f.readlines()
        f.close()
        last_command = list_commands[-2].split(';')[1]
        return last_command
    except Exception, e:
        print e
        raise Exception, "Cannot get zsh last command"


def get_bash_last_command():
    try:
        with open(os.path.expanduser("~/.bash_history"), "r") as f:
            list_commands = f.readlines()
        f.close()
        last_command = list_commands[-2]
        return last_command
    except Exception, e:
        print e
        raise Exception, "Cannot get bash last command"


def get_shell():
    environ = os.environ["SHELL"]
    shell = environ.split('/')[2]
    return shell


def get_last_command():
    config_bashrc()
    shell = get_shell()

    if shell == 'bash':
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
