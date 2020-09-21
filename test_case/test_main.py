# -*- coding:utf-8 -*-

import pytest
from api.send_request import BaseRequest
from common.db_utils import DB_Utils
from common.read_config import ReadConfig
from common.read_excel import ReadExcel
from loguru import logger

class TestMain(object):

    data_list = ReadExcel("excel_path_1").read_excel()
    logger.info(f"data is {data_list}")

    @pytest.mark.parametrize("method, url, data, result, status, parametric_key, header", data_list)
    def test_001(self, method, url, data, result, status, parametric_key, header):
        real_res = BaseRequest().base_requests(method, url, parametric_key, data, header, file_var=None, file_path=None)
        # logger.info(f"测试用例结果为{}")
        assert result == real_res

if __name__ == '__main__':
    # TestMain().init_data("excel_path_1")
    pass