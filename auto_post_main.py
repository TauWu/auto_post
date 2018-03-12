# -*- coding: utf-8 -*-
# 自动发帖主程序

from module.database.user import User
from util.common.logger import base_info, base_err
from constant.dict import *
from sys import argv

def user_cmd(opt_id):
    user = User()
    opt = user_cmd_dict[str(opt_id)]

    username = input("请输入需要%s操作的用户名\n"%opt)
    try:
        if opt_id == 3:
            pwd = user.get_user_password(username)
            print("用户【%s】的信息如下\n密码：%s\n用户类型：%s"%(pwd[0],pwd[1],user_type_dict[str(pwd[2])]))
        else:
            password = input("请输入需要%s操作的密码\n"%opt)
            usertype = int(input("\n请输入需要%s操作的用户类型 1-只有安居客 2-既有安居客又有58同城\n"%opt))
            if usertype not in [1, 2]:
                raise ValueError("用户类型错误！")

            if opt_id == 1:
                '''新增'''
                user.insert_user(username, password, usertype)
            elif opt_id == 2:
                '''修改'''
                user.update_user(username, password, usertype)
            else:
                raise ValueError("没有这个操作")
    except Exception as e:
        base_err(str(e))
    finally:
        user.close

if __name__ == '__main__':
    if len(argv) == 2:
        '''带参数的执行程序'''
        if argv[1].strip() == "user":
            while True:
                opt_id = int(input("请输入需要进行的用户操作：\n【0】退出程序\n【1】新增用户\n【2】修改用户\n【3】查看用户\n\n"))
                if opt_id > 0 and opt_id <= 3:
                    user_cmd(opt_id)
                elif opt_id == 0:
                    break
                else:
                    print("没有这个操作【%d】"%opt_id)
                    pass