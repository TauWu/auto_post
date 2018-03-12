# 用户表操作
from util.database import DBController
from util.common.logger import use_logger

@use_logger(level="info")
def db_info(msg):
    pass

@use_logger(level="err")
def db_err(msg):
    pass

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

    def insert_user(self, username, password, usertype, name=""):
        '''向表中插入一条数据'''
        from .sql_template import insert_user_sql

        sql_execute = insert_user_sql.format(username=username, password=password,\
        usertype=usertype, name=name)

        try:
            self.execute(sql_execute)
        except Exception as e:
            db_err("向用户表中插入一条数据失败！ e:%s, SQL: %s"%(str(e),sql_execute.replace('\n','')))

    def user_exist(self, username):
        '''查询某一用户在数据表中是否存在 返回布尔值'''
        try:
            rtn = self.get_user_password(username)
        except ValueError:
            return False
        return True
    
    def update_user(self, username, password, usertype, name=""):
        '''更新某一用户的账户信息'''
        from .sql_template import update_user_sql

        sql_execute = update_user_sql.format(username=username, password=password,\
        usertype=usertype, name=name)

        try:
            self.execute(sql_execute)
        except Exception as e:
            db_err("修改用户表中【{username}】信息错误！".format(user_name=username))

    @property
    def close(self):
        DBController.close