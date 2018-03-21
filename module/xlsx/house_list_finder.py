# -*- coding: utf-8 -*-
# 获取某一文件夹内部的所有表格文件并返回

import os

class HouseListFinder():
    '''房源表格搜寻器'''

    def __init__(self, path="/data/docs"):
        self.path = path                # 父路径
        self.house_file_list = list()   # 房源文件路径列表
        self.__load_xlsx__
    
    @property
    def __load_xlsx__(self):
        '''遍历目录下所有的xlsx文件'''

        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file[-4:] == "xlsx":
                    '''只收集Excel文件'''
                    self.house_file_list.append(os.path.abspath(os.path.join(os.getcwd(), root, file)))

if __name__ == "__main__":
    finder = HouseListFinder("/data/docs").house_file_list