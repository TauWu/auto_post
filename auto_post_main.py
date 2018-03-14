#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 自动发帖主程序

from sys import argv

from module.database.user import User
from module.database.house_info import HouseInfoXlsx
from module.sele.send_house import SendHouse

from constant.logger import unknown, base_info, base_warn, base_err, base_fatal
from constant.dict import *

def user_cmd(opt_id, username=""):
    '''用户信息操作命令'''
    user = User()
    opt = user_cmd_dict[str(opt_id)]

    try:
        if opt_id == 3:
            pwd = user.get_user_password(username)
            print("用户【%s】的信息如下\n密码：%s\n用户类型：%s"%(pwd[0],pwd[1],user_type_dict[str(pwd[2])]))
        elif opt_id == 4:
            print("当前查询到的用户名有...\n\n%s\n"%"\n".join([user[0] for user in user.all_users]))
        else:
            password = input("请输入用户[%s]进行%s操作的密码\n"%(username, opt))
            usertype = int(input("请输入需要%s操作的用户类型 1-只有安居客 2-既有安居客又有58同城\n"%opt))
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

def send_cmd(username):
    '''登录操作命令'''
    user = User()
    is_exist = user.user_exist(username)
    if not is_exist:
        base_warn("没有找到用户名为[%s]的用户，继续操作将为您新增此用户..."%username)
        user_cmd(1, username)
    else:
        base_info("用户[%s]开始尝试登录..."%username)
        sender = SendHouse(username, [['总门店', 1, '新城枫景', '6', '13', '19', '800', '【图片实拍 月付】精装修 紧靠地铁站 品牌家电拎包入住']])
        fact = sender.send
        for f in fact:
            print(f)
            a = input("DEBUG")

if __name__ == '__main__':

    if len(argv) == 1:
        username = input("请输入需要登录的用户名\n")
        send_cmd(username)


    if len(argv) == 2:
        '''带参数的执行程序'''

        if argv[1].strip() == "user":
            '''用户信息维护操作'''
            while True:
                opt_id = int(input("请输入需要进行的用户操作：\n【0】退出程序\n【1】新增用户\n【2】修改用户\n【3】查看用户\n【4】查询所有用户名\n"))
                if opt_id > 0 and opt_id <= 3:
                    username = input("请输入需要操作的用户名\n")
                    user_cmd(opt_id, username)
                elif opt_id == 4:
                    user_cmd(opt_id)
                elif opt_id == 0:
                    break
                else:
                    base_warn("没有这个操作【%d】"%opt_id)
                    pass
        
        elif argv[1].strip() == "import":
            '''数据导入操作'''
            try:
                x = HouseInfoXlsx("house_list.xlsx")
                x.insert_data
            except FileNotFoundError:
                base_fatal("没有找到该文件！请检查！")
                raise
            except Exception:
                unknown(Exception)
                raise
        
        elif argv[1].strip() == "send":
            '''发送操作'''
            username = input("请输入需要登录的用户名\n")
            send_cmd(username)