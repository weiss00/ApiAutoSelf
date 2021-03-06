# -*- coding: utf-8 -*-

import xlrd
import openpyxl
from common.read_config import ReadConfig
from loguru import logger

class ReadExcel(object):

    def __init__(self, file_key):
        """
        :param file_key: 配置文件中  【文件的key】
        """
        self.excel_config = ReadConfig(file_key).read_config_keyword()
        # logger.info(self.excel_config)

    def read_excel(self):
        wb = xlrd.open_workbook(self.excel_config)
        test_data = []
        try:
            sheet = wb.sheet_by_index(0)
        # 获取最大行数和列数
            nrows = sheet.nrows
            # logger.info(f"行数为{nrows}") 
            ncols = sheet.ncols
            # logger.info(f"列数为{ncols}")
            if nrows > 1:
                keys = sheet.row_values(0)
                # logger.info(f"第一行数据为{keys}")
            for row in range(1, nrows):
                values = sheet.row_values(row)
                # 去除用例标题
                values.pop(0)
                test_data.append(values)
            # print(test_data)
            return test_data
        except Exception as e:
            logger.error(f"excel表格可能无数据, 重新检查 ========>{e}")

    def write_back(self, row, col, result):
        wb = openpyxl.load_workbook(self.excel_config)
        sheet = wb.index(0)
        sheet.cell(row, col).value = result
        wb.save(self.excel_config)
        

if __name__ == '__main__':
    ed = ReadExcel("excel_path_1")
    datas = ed.read_excel()
    print(datas[0])