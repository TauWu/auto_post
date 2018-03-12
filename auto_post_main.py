# -*- coding: utf-8 -*-
# 自动发帖主程序

from module.database.user import User
from util.common.logger import base_info

if __name__ == '__main__':
    try:
        user = User()
        user.insert_user("测试用户","测试密码",1,"测试中文名")
        print(user.get_user_password('测试用户'))
        print(user.user_exist("啊哈"))
        user.update_user("测试用户","2133123",1,"testName")
        print(user.get_user_password('测试用户'))
    except Exception as e:
        base_info(str(e))
    finally:
        user.close