# -*- coding: utf-8 -*-

import json
import jsonpath
from common.operation_excel import Operation_Excel
from common.save_resp import Save_Resp
from api.run_method import RunMethod
from data.get_data import Get_Data
from tools.log import Log
from loguru import logger

"""
    处理依赖数据的工具类
"""

class Dependent_Data(object):

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = Operation_Excel()
        self.get_data = Get_Data()
        self.log = Log()
        self.row_index = self.opera_excel.get_index_caseId(self.case_id)


    # 根据传入的case_id 获取该行数据
    def get_case_line_data(self):
        row_data = self.opera_excel.get_rowData_caseId(self.case_id)
        return row_data

    # 执行依赖数据, 获取结果
    def run_method(self):
        run_method = RunMethod()
        request_data = self.get_data.get_data_for_json(self.row_index)
        method = self.get_data.get_request_method(self.row_index)
        url = self.get_data.get_url(self.row_index)
        header = self.get_data.is_header(self.row_index)
        res = run_method.run_main(method, url, request_data, header)
        logger.info(f"request_data is {request_data}, index is {self.row_index}, resp is {res}")
        return res


    # 根据依赖的key去获取执行依赖测试case的响应，然后返回对应的值
    def get_resp_caseResult(self, data, row):
        # 得到该case的依赖表达式
        depend_expr = self.get_data.get_depend_expr(row)
        logger.info(f"expr === {depend_expr}, type === {type(depend_expr)}")
        # 查询到依赖数据所依赖的字段
        data_key = self.get_data.get_depend_dataName(row)
        logger.info(f"expr_data_key is {data_key}")
        # 根据依赖表达式获取响应的结果
        # data_value = jsonpath.jsonpath(json.loads(self.run_method()), depend_expr)[0]
        data_value = Save_Resp.expr_data(data, depend_expr)
        logger.info(f"expr_data_value is {data_value}")
        return data_key, data_value
    #
    def test_1(self):
        depend_expr = self.get_data.get_depend_expr(2)
        res = '{"mobile":"18844077709"}'
        data_key = self.get_data.get_depend_dataName(2)
        data_value = jsonpath.jsonpath(json.loads(res), depend_expr)[0]
        return data_value

if __name__ == '__main__':
    dep = Dependent_Data("demo-2")
    key, value = dep.test_1()
    print(f"data_key is {key}, data_value is {value} =====> type is {type(key), type(value)}")