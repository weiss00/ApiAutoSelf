# -*- coding:utf-8 -*-
import json

from loguru import logger
from api.run_method import RunMethod
from common.get_token import Get_Token
from common.is_contain import Is_Contain
from common.save_resp import Save_Resp
from data.get_data import Get_Data
from data.dependent_data import Dependent_Data

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = Get_Data()
        self.compare = Is_Contain()
        self.save_res = Save_Resp()
        # self.depend_data = Dependent_Data()
        self.resp_data = {}

    # 程序执行
    def go_on_run(self):
        header = None
        res = None
        pass_count = []
        fail_count = []
        rows_counts = self.get_data.get_lines()
        for i in range(1, rows_counts):
            is_run = self.get_data.is_Run(i)
            method = self.get_data.get_request_method(i)
            url = self.get_data.get_url(i)
            data = self.get_data.get_data_for_json(i)
            logger.info(f"request_data is {data}, type ====> {type(data)}")
            expect_data = self.get_data.get_except_data(i)
            header = self.get_data.is_header(i)

    # 判断该条case是否有依赖数据
            depend_id = self.get_data.get_depend_caseId(i)
            if depend_id:
                depend_data = Dependent_Data(depend_id)
                # 根据依赖表达式，获取依赖的数据以及依赖的字段
                depend_key, depend_value = depend_data.get_resp_caseResult(self.resp_data, i)
                logger.info(f"depend_value =====> {depend_value}")
                data[depend_key] = depend_value
                # 更新请求数据
                logger.info(f"request_data_2 is {data}, type ====> {type(data)}")

    #      method, url, data, header
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                logger.info(f"res is type {type(res)}")
                # if ("token" in res):
                #     Get_Token.get_header(res['token'])
                self.save_res.save_opt(self.resp_data, self.get_data.get_id(i), json.loads(res))
                compare_result = self.compare.is_contain(expect_data, res)
                if compare_result:
                    self.get_data.write_result(i, "pass")
                    pass_count.append(i)
                else:
                    self.get_data.write_result(i, res)
                    fail_count.append(i)
        logger.info(f"data is {self.resp_data}")

if __name__ == '__main__':
    res = RunTest().go_on_run()
