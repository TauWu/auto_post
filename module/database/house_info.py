# 房源信息表操作
from util.database import DBController
from module.xlsx.house_list_reader import HouseListReader
from constant.logger import db_err, db_fatal

class HouseInfo(DBController):

    def __init__(self):
        DBController.__init__(self)

    def insert_house_info(self, house_info):
        '''插入房源信息'''
        from .sql_template import insert_house_info_sql

        sql_execute = insert_house_info_sql%house_info

        try:
            self.execute(sql_execute)
        except Exception as e:
            db_err("向房源表中插入一条数据失败！e:%s, SQL: %s"%(str(e),sql_execute))

    @property
    def truncate_house_info(self):
        '''清空数据表'''
        sql_execute = "truncate table auto_post_house_info"
        try:
            self.execute(sql_execute)
        except Exception as e:
            db_fatal("清空数据表失败！e:%s, SQL: %s"%(str(e),sql_execute))
            raise e

class HouseInfoXlsx(HouseInfo, HouseListReader):

    def __init__(self, filename):
        HouseInfo.__init__(self)
        HouseListReader.__init__(self, filename)
        self.house_info = self.vaild_data

    @property
    def insert_data(self):
        for house_info in self.house_info:
            self.insert_house_info(house_info)
