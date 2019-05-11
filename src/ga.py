#!/usr/local/bin/python3

import subprocess
import os
import datetime
from sys import argv

def main():
    git_add_command(argv)

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

def write_changelog(content):
    content = content.replace('\\n', '')
    try:
        f = open('changelog.txt', "a+")
        try:
            f.write(f"{content}\r\n")
            print(f"wrote: {content} to changelog.txt")
        finally:
            f.close()
    except IOError:
        print('failed to write to changelog.txt')
  
    return


def git_add_command(comment):
    cwd = os.getcwd()

    # Get the output from running my GA command.
    result = subprocess.run(['git', 'commit', '-a', '-m', comment[1]], stdout=subprocess.PIPE)
    print(result.stdout)
    
    # Change directory to this repo
    homedir = os.environ['HOME']
    os.chdir(f'{homedir}/Github/work-tracker/src')
    print('Changed directory')

    content = f'{get_time()}:  {result.stdout}'
    # Write the result to my changelog.txt file in this repo.
    write_changelog(content)

    work_result = subprocess.run(['git', 'commit', '-a', '-m', "updating changelog"], stdout=subprocess.PIPE)
    print(work_result.stdout)

    push_result = subprocess.run(['git', 'push'], stdout=subprocess.PIPE)
    print(push_result.stdout)

    print(f'Changing back to {cwd}')
    os.chdir(cwd)

    return

if __name__ == "__main__":
    main()