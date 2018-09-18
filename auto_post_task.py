#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def check_exists():
    '''
    check `./task.sh` file exists.

    '''
    if os.access("./task.sh", 000):
        os.remove("./task.sh")

if __name__ == "__main__":
    check_exists()

    user_list = list()
    while True:
        user = input("Add User Name ...")
        if user == "":
            break
        else:
            user_list.append(user)

    with open("task.sh", "w") as f:
        for user in user_list:
            f.write("python3 auto_post_main.py start %s \n"%user)

    os.chmod("./task.sh", 777)