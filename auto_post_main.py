# -*- coding: utf-8 -*-
# 自动发帖主程序

from module.database.user import User

if __name__ == '__main__':
    user = User()
    pwd = user.get_user_password('yjgy662')
    print(pwd)