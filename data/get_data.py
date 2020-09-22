# -*- coding:utf-8 -*-

from loguru import logger
from data.data_config import Global_Var
from common.operation_excel import Operation_Excel
from common.operation_json import Operation_Json
from common.get_token import Get_Token

"""
获取excel中特定数据工具类
"""

class Get_Data(object):

    def __init__(self):
        self.data_config = Global_Var()
        self.opera_excel = Operation_Excel()
        self.opera_json = Operation_Json()

    # 获取excel行数， 也就是case个数 - 1
    def get_lines(self):
        return self.opera_excel.get_rows()

    # 判断是否执行
    def is_Run(self, row):
        flag = None
        status = self.opera_excel.get_cell_value(row, Global_Var.get_run())
        if status == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        is_header = self.opera_excel.get_cell_value(row, Global_Var.get_header())
        if is_header == "yes":
            return Get_Token.token
        else:
            return None
    # 获取请求方式
    def get_request_method(self, row):
        request_method = self.opera_excel.get_cell_value(row, Global_Var.get_request_method())
        return request_method

    # 获取请求url
    def get_url(self, row):
        target_url = self.opera_excel.get_cell_value(row, Global_Var.get_url())
        return target_url

    # 获取请求数据
    def get_request_data(self, row):
        data = self.opera_excel.get_cell_value(row, Global_Var.get_request_data())
        if data == '':
            return None
        return data

    # 通过关键字拿到data数据
    def get_data_for_json(self, row):
        data = self.opera_json.get_data(self.get_request_data(row))
        if data == "":
            return None
        return data

    # 获取预期结果
    def get_except_data(self, row):
        except_data = self.opera_excel.get_cell_value(row, Global_Var.get_except())
        if except_data == '':
            return None
        return except_data

    # 向excel复制表中写数据
    def write_result(self, row , value):
        col = Global_Var.get_result()
        self.opera_excel.write_excel(row, col, value)


if __name__ == '__main__':
    excel = Get_Data()
    header = excel.is_header(4)
    logger.info(f"reqeust_json is {header}")