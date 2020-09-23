# -*- coding: utf-8 -*-

import json
import jsonpath
from common.operation_excel import Operation_Excel
from api.run_method import RunMethod
from data.get_data import Get_Data

"""
    处理依赖数据的工具类
"""

class Dependent_Data(object):

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = Operation_Excel()
        self.get_data = Get_Data()
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
        return res

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_resp_caseResult(self, row):
        data = {}
        depend_expr = self.get_data.get_depend_expr(row)
        data_key = self.get_data.get_depend_dataName(row)
        data_value = jsonpath.jsonpath(json.loads(self.run_method()), depend_expr)[0]
        data[data_key] = data_value
        return data

if __name__ == '__main__':
    dep = Dependent_Data("demo-2")
    dep.get_resp_caseResult()