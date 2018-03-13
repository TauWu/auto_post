# -*- coding: utf-8 -*-

from util.common.xlsx_reader import XlsxReader
from constant.list import houseinfo_sheet_comfirm_list

def single_dict(indict):
    keys = indict.keys()
    values = indict.values()
    if len(keys) > 1 or len(values) > 1:
        raise ValueError("只能取值只有一个K-V的字典")
    else:
        return list(keys)[0], list(values)[0]

def vaild_content(sheetname, index, content):
    '''验证函数 传入一个待确认的列表list 户型和定价方式不做验证'''
    try:
        community_name = content[0]
        splited_floor = content[1].strip().split('/')
        full_address = content[2].strip()
        house_title = content[7].strip()

        if len(community_name) == 0:
            raise RuntimeError("序号[%d] 小区名称为空" % index)

        if len(full_address) == 0:
            raise RuntimeError("序号[%d] 完整地址为空" % index)

        if len(house_title) == 0:
            raise RuntimeError("序号[%d] 房源标题为空" % index)

        try:
            index = int(index)
        except Exception:
            raise RuntimeError("序号[%d] 不是数字" % index)

        try:
            current_floor = int(splited_floor[0])
        except Exception:
            raise RuntimeError("序号[%d] 当前楼层不是数字" % index)

        try:
            total_floor = int(splited_floor[1])
        except Exception:
            raise RuntimeError("序号[%d] 总楼层不是数字" % index)

        try:
            total_area = int(content[4])
        except Exception:
            raise RuntimeError("序号[%d] 总面积不是数字" % index)

        try:
            rent_money = int(content[5])
        except Exception:
            raise RuntimeError("序号[%d] 租金不是数字" % index)

    except Exception as e:
        print("表格[%s] %s 该条数据已经忽略"%(sheetname, str(e)))
        return None

    else:
        return sheetname, index, community_name, current_floor,\
        total_floor, full_address, total_area, rent_money, house_title
        
    

class HouseListReader(XlsxReader):

    def __init__(self, filename):
        XlsxReader.__init__(self, filename)
        self.filename = filename
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
                print("表格[%s] 的标题不正确 该张表数据已全部忽略"%single_dict(title)[0])
        return self.comfirm_sheet
    
    @property
    def vaild_contents(self):
        '''验证数据'''
        for sheetname in self.comfirm_sheet:
            contents = self.get_sheet_contents(sheetname)
            for content in contents:
                vaild_rtn = vaild_content(sheetname, single_dict(content)[0], single_dict(content)[1])
                if vaild_rtn is not None:
                    self.comfirm_house_info.append(vaild_rtn)
        return self.comfirm_house_info

    @property
    def vaild_data(self):
        '''清洗数据并返回'''
        self.vaild_titles
        self.vaild_contents
        return self.comfirm_house_info