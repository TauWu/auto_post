# 用户表操作
from util.database import DBController

class User(DBController):

    def __init__(self):
        DBController.__init__(self)

    def get_user_password(self, username):
        '''通过用户名获取用户密码'''
        from .sql_template import get_user_password_sql

        sql_execute = get_user_password_sql.format(username=username)
        self.execute(sql_execute)

        rtn = self.cur.fetchone()

        if rtn is not None:
            return rtn
        else:
            raise ValueError("数据表中没有这个用户！")
