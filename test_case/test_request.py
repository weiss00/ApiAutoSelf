# -*- coding: utf-8 -*-

from api.send_request import BaseRequest
from common.read_excel import ReadExcel
from loguru import logger
import json
from common.db_utils import DB_Utils

class Test_Req(object):

    def __init__(self):
        self.data_list = ReadExcel("excel_path_1").read_excel()
        # logger.info(f"获得的数据列表为{self.data_list}")
        self.request = BaseRequest()

    def get_code(self):
        param = self.data_list[0]
        print(param[2])
        data = json.loads(param[2])
        print(data)
        res = self.request.base_requests(param[0], param[1], param[5], data)
        logger.info(f"info is {res}")
        sql = f"select code from users_verifycode where mobile = '{data['mobile']}';"
        code = DB_Utils().select_item(sql)
        logger.info(f"code is {code}")
        return code

if __name__ == '__main__':
    req = Test_Req()
    req.get_code()