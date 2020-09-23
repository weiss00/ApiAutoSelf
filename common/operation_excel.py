# -*- coding:utf-8 -*-

import xlrd
from xlutils.copy import copy
from common.read_config import ReadConfig
from tools.time_format import Time_Format

class Operation_Excel(object):

    def __init__(self):
        self.excel_path = ReadConfig().read_config_keyword("excel_path_1")
        self.book = xlrd.open_workbook(self.excel_path)
        self.table = self.book.sheet_by_index(0)
        self.excel_copy = ""
        self.copy_book = ""
        self.copy_table = ""

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
    # 将测试结果写入到excel中
    def write_excel(self, row, col, value):
        if self.copy_book == "":
            self.copy_book = copy(self.book)
            self.copy_table = self.copy_book.get_sheet(0)
            self.copy_table.write(row, col, value)
            new_path = f"../test_data/result/result_{Time_Format.format_time()}.xls"
            self.copy_book.save(new_path)
        else:
            self.copy_table.write(row, col, value)
            new_path = f"../test_data/result/result_{Time_Format.format_time()}.xls"
            self.copy_book.save(new_path)

    # 根据列号获取整列数据
    def get_colData_index(self, col_num=None):
        if col_num != None:
            col_datas = self.table.col_values(col_num)
        else:
            col_datas = self.table.col_values(0)
        return col_datas

    #  传行数获得整行数据
    def get_rowData_index(self, num):
        row_data= self.table.row_values(num)
        return row_data

    # 传入case_id 得到该case_id所在的行数
    def get_index_caseId(self, case_id):
        num = 0
        cols_data = self.get_colData_index()
        for col_data in cols_data:
            if case_id == col_data:
                return num
            num += 1
        return num

    # 传入case_id 返回该case_id的行内容
    def get_rowData_caseId(self, case_id):
        num = self.get_index_caseId(case_id)
        row_data = self.get_rowData_index(num)
        return row_data

if __name__ == '__main__':
    c = Operation_Excel()
    count = c.get_index_caseId("demo-1")
    print(count)