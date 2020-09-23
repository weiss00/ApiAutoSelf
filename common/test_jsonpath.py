# -*- coding:utf-8 -*-

import json
import jsonpath
from common.read_config import ReadConfig
from common.operation_json import Operation_Json

class Test_JsonPath(object):

    def __init__(self):
        # ReadConfig().read_config_keyword("json_path")
        self.opera_json = Operation_Json()

    def test_get_jsonData(self):
        users = self.opera_json.get_data("users")
        code = self.opera_json.get_data("code")
        data = users["username"]
        format_data = jsonpath.jsonpath(code, data)
        print(format_data[0])

if __name__ == '__main__':
    Test_JsonPath().test_get_jsonData()