# -*- coding:utf-8 -*-

import pytest
from api.run_method import RunMethod
from data.get_data import Get_Data
from loguru import logger
from common.get_token import Get_Token
from common.is_contain import Is_Contain

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = Get_Data()
        self.compare = Is_Contain()

    # 程序执行
    def go_on_run(self):
        header = None
        res = None
        rows_counts = self.get_data.get_lines()
        for i in range(1, rows_counts):
            is_run = self.get_data.is_Run(i)
            method = self.get_data.get_request_method(i)
            url = self.get_data.get_url(i)
            data = self.get_data.get_data_for_json(i)
            expect_data = self.get_data.get_except_data(i)
            header = self.get_data.is_header(i)
    #         method, url, data, header
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                compare_result = self.compare.is_contain(expect_data, res)
                if compare_result:
                    print("测试通过")
                else:
                    print("测试失败")
                logger.info(f" res is =========> {res}")
                if("token" in res):
                    Get_Token.get_header(res['token'])
                    return
        return res

    # def test_demo(self):

if __name__ == '__main__':
    res = RunTest().go_on_run()
    # logger.info(f"res is {res}")