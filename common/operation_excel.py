# -*- coding:utf-8 -*-

import xlrd
from common.read_config import ReadConfig

class Operation_Excel(object):

    def __init__(self):
        self.excel_path = ReadConfig().read_config_keyword("excel_path_1")
        self.book = xlrd.open_workbook(self.excel_path)
        self.table = self.book.sheet_by_index(0)

    # 获取excel的sheet表
    # def get_sheet(self, index=0):
    #     return self.book.sheet_by_index(index)

    #  获取excel总行数
    def get_rows(self):
        return self.table.nrows

    # 获取excel总列数
    def get_cols(self):
        return self.table.ncols

    # 获取特定单元格
    def get_cell(self, row, col):
        return self.table.cell(row, col)

    # 获取excel单元格的值
    def get_cell_value(self, row, col):
        return self.table.cell_value(row, col)

if __name__ == '__main__':
    # value = Operation_Excel().get_cell_value(2, 1)
    rows = Operation_Excel().get_rows()
    print(rows)