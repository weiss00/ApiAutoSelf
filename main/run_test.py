# -*- coding:utf-8 -*-

from loguru import logger
from api.run_method import RunMethod
from common.get_token import Get_Token
from common.is_contain import Is_Contain
from data.get_data import Get_Data

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
            logger.info(f"data is {data}")
            expect_data = self.get_data.get_except_data(i)
            # logger.info(f"预期结果为 === > {expect_data}")
            header = self.get_data.is_header(i)

    #         method, url, data, header
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                # if ("token" in res):
                #     Get_Token.get_header(res['token'])
                compare_result = self.compare.is_contain(expect_data, res)
                if compare_result:
                    self.get_data.write_result(i, "pass")
                else:
                    self.get_data.write_result(i, "fail")
                # logger.info(f" res is =========> {res}")

    # def test_demo(self):

if __name__ == '__main__':
    res = RunTest().go_on_run()
