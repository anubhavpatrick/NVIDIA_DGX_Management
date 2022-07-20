"""Python script to create users 
Reference - https://stackoverflow.com/questions/13045593/using-sudo-with-python-script 
"""

from subprocess import Popen, PIPE
from getpass import getpass
import os

sudo_password = getpass('Input your su password')

ch = input('Do you want to add multiple users simultaneouly? [y/Y]')

if ch.upper()=='Y':
    prefix = input('Enter prefix of usernames ')
    num_of_users = int(input('Enter number of users '))
    usernames = []
    for i in range(num_of_users):
        usernames.append(f'{prefix}{i}')
else:
    usernames = []
    usernames.append(input('Enter username '))

for user in usernames:
    #Adding user
    useradd_command = f'useradd -m -s /bin/bash {user}'.split()
    u = Popen(['sudo', '-S'] + useradd_command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    sudo_prompt = u.communicate(sudo_password + '\n')[1]

    #Updating password as identical to username
    passwd_command = f'passwd {user}'.split()
    p = Popen(['sudo', '-S'] + passwd_command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    sudo_prompt = p.communicate(f'{user}\n{user}\n')[1]
    print(sudo_prompt)

    #Adding user to Docker group
    docker_grp_command = f'gpasswd -a {user} docker'.split()
    d = Popen(['sudo', '-S'] + docker_grp_command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    sudo_prompt = d.communicate(sudo_password +'\n')[1]
    

os.system('newgrp docker')    

print('List of users\n')
os.system('cut -d : -f 1 /etc/passwd')

print(f'\n*** {len(usernames)} User(s) successfully created: {usernames}***')
