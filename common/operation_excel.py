# -*- coding:utf-8 -*-

import time
import os
import xlrd
from xlutils.copy import copy
from common.read_config import ReadConfig

class Operation_Excel(object):

    def __init__(self):
        self.excel_path = ReadConfig().read_config_keyword("excel_path_1")
        self.book = xlrd.open_workbook(self.excel_path)
        self.table = self.book.sheet_by_index(0)
        self.excel_copy = ""
        self.copy_book = ""
        self.copy_table = ""

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

    '''
       #2  测试结果写入
           # 文件不存在 -- 新建excel -- 写 -- xlwt
           # 文件本身存在 -- 另存写新excel -- xlutils
           from xlutils.copy import copy   
           #1 - 拷贝excel对象
           newWorkBook = copy(workBook)
           #2 - 取拷贝的excel的sheet---sheet 下标
           newSheet = newWorkBook.get_sheet(1)
           #3 - 写入数据 -- info -- newSheet.write(行下标，列下标，内容)
           newSheet.write(1, 9, info)
           #4 - 保存excel对象
           newWorkBook.save(r'../data/res.xls')
       '''

    def write_excel(self, row, col, value):
        if os.path.exists(self.excel_copy) == False:
            self.copy_book = copy(self.book)
            self.copy_table = self.copy_book.get_sheet(0)
            self.copy_table.write(row, col, value)
            self.excel_copy = ReadConfig().read_config_keyword("excel_copy")
            # time_format = time.strftime('%Y%m%d-%H%M%S', time.localtime())
            self.copy_book.save(self.excel_copy)
        else:
            self.copy_table.write(row, col, value)
            self.copy_book.save(self.excel_copy)

if __name__ == '__main__':
    Operation_Excel().write_excel(4, 4, "asda")