# -*- coding: utf-8 -*-

from util.common.xlsx_reader import XlsxReader
from constant.list import houseinfo_sheet_comfirm_list
from constant.logger import vld_err

def single_dict(indict):
    keys = indict.keys()
    values = indict.values()
    if len(keys) > 1 or len(values) > 1:
        raise ValueError("只能取值只有一个K-V的字典")
    else:
        return list(keys)[0], list(values)[0]

def vaild_content(filename, sheetname, index, content):
    '''验证函数 传入一个待确认的列表list 户型和定价方式不做验证'''
    try:
        community_name = content[0]
        try:
            splited_floor = content[1].strip().split('/')
        except Exception:
            raise RuntimeError("楼层信息有误")
        full_address = content[2].strip()
        house_title = content[7].strip()
        house_type = int(content[3].strip()[0])
        store = content[8].strip()

        if len(community_name) == 0:
            raise RuntimeError("小区名称为空")

        if len(full_address) == 0:
            raise RuntimeError("完整地址为空")

        if len(house_title) == 0:
            raise RuntimeError("房源标题为空")

        try:
            index = int(index)
        except Exception:
            raise RuntimeError("序号不是数字")

        try:
            current_floor = int(splited_floor[0])
        except Exception:
            raise RuntimeError("当前楼层不是数字")

        try:
            total_floor = int(splited_floor[1])
        except Exception:
            raise RuntimeError("总楼层不是数字")

        try:
            total_area = int(content[4])
        except Exception:
            raise RuntimeError("总面积不是数字")

        try:
            rent_money = int(content[5])
        except Exception:
            raise RuntimeError("租金不是数字")

    except Exception as e:
        vld_err("文件[%s] 表格[%s] 序号[%s] %s 该条数据已经忽略"%(filename, sheetname, str(index), str(e)))
        return None

    else:
        return (sheetname, index, community_name, current_floor,\
        total_floor, full_address, total_area, rent_money, house_title,\
        house_type, store)
        
    

class HouseListReader(XlsxReader):

    def __init__(self, filename):
        XlsxReader.__init__(self, filename)
        self.filename = filename
        self.file = self.filename.split('/')[-1][:-5]
        self.comfirm_sheet = list()
        self.comfirm_house_info = list()

    @property
    def vaild_titles(self):
        '''验证标题'''
        titles = self.titles
        for title in titles:
            if single_dict(title)[1] == houseinfo_sheet_comfirm_list:
                self.comfirm_sheet.append(single_dict(title)[0])
            else:
                vld_err("文件[%s] 表格[%s] 的标题不正确 该张表数据已全部忽略"%(self.file, single_dict(title)[0]))
        return self.comfirm_sheet
    
    @property
    def vaild_contents(self):
        '''验证数据'''
        for sheetname in self.comfirm_sheet:
            contents = self.get_sheet_contents(sheetname)
            for content in contents:
                vaild_rtn = vaild_content(self.file, sheetname, single_dict(content)[0], single_dict(content)[1])
                if vaild_rtn is not None:
                    vaild_rtn = list(vaild_rtn)
                    vaild_rtn.insert(0, self.file)
                    self.comfirm_house_info.append(tuple(vaild_rtn))
        return self.comfirm_house_info

    @property
    def vaild_data(self):
        '''清洗数据并返回'''
        self.vaild_titles
        self.vaild_contents
        return self.comfirm_house_info