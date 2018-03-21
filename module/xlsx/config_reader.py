# -*- coding: utf-8 -*-

from util.common.xlsx_reader import XlsxReader

class ConfigReader(XlsxReader):

    def __init__(self,filename):
        XlsxReader.__init__(self, filename)
        self.filename = filename
        self.order_list = list()
        self.__read_order__

    @property
    def __read_order__(self):
        cont_dict = self.contents_dict[0]['1']
        for i in range(1, len(cont_dict) + 1):
            self.order_list.append(cont_dict[i-1][str(i)])
    @property
    def store_list(self):
        stores = list()
        for order in self.order_list:
            stores.append(order[0])
        return stores

    @property
    def size_list(self):
        sizes = list()
        for order in self.order_list:
            sizes.append(order[1])
        return sizes