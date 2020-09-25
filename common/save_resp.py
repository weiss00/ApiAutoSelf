# -*- coding:utf-8 -*-

"""
将执行后的case实际结果以相对应格式保存
该工具类便于对依赖数据进行处理
"""

import json
from loguru import logger
from jsonpath import jsonpath

class Save_Resp(object):

    @classmethod
    def save_opt(self, data_container, key, value):
        """
        格式为 ：  { "case_id" : resp }
        :return:  { "case_1" : resp1, "case_2" : resp2, "case_3" : resp3 ....}
        """
        data_container[key] = value

    @classmethod
    def expr_data(self, data, expr):
        data = jsonpath(data, expr)[0]
        return data

if __name__ == '__main__':
    save = Save_Resp()
    value = {"mobile":"123456"}
    save.save_opt("username1", value)
    expr = "$.username1.mobile"
    save.expr_data(expr)


    # save.expr_format("$.username1.mobile")