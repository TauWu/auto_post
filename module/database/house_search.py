# 搜索房源模块
from util.database import DBController
from constant.logger import db_err, db_fatal

class HouseSearch(DBController):

    def __init__(self, store, size=20, housetype=1, source=1):
        DBController.__init__(self)
        self.store = store                  # 所属门店
        self.size  = size                   # 推送条数
        self.source = source                # 房源来源（1-推广 2-本地）
        self.housetype = housetype          # 房型
        self.house_list = list()            # 搜索结果（size的两倍）
        self.__search_house_list__          # 执行搜索操作
    
    @property
    def __search_house_list__(self):
        from .sql_template import house_search_sql
        from random import sample
        
        limit_str = "limit %d"%(5*self.size)    # 从最多五倍size的数据里面抽取size数量的房源
        where_str = "where store = '%s' and house_type = %d and source = %d"%(self.store, self.housetype, self.source)
        
        execute_sql = house_search_sql%(where_str, limit_str)

        try:
            self.execute(execute_sql)
        except Exception as e:
            db_fatal("搜索房源错误！")
            raise
        
        db_rtn = [list(house_info) for house_info in self.cur.fetchall()]

        if len(db_rtn) <= 2*self.size:
            self.house_list = db_rtn
        else:
            self.house_list = sample(db_rtn, 2*self.size)