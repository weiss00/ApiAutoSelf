# -*- coding:utf-8 -*-

import json
import requests
from mock.mock_func import Mock_Test

"""
    简单封装get / post 基类
"""

class RunMethod(object):


    def post_main(self, url, data, header=None):
        res = None
        if header == None:
            res = requests.post(url=url, data=data)
        else:
            res = requests.post(url=url, data=data, headers=header)
        print(res.status_code)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header == None:
            res = requests.get(url=url, data=data)
        else:
            res = requests.get(url=url, data=data, headers=header)
        return res.json()

    def run_main(self, method, url, data, header):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True)

#     mock 模拟请求
#     mock_method, request_data, url, method, response_data
    def mock_test(self, method, url, data, header=None):
        mock_response = {"success":200}
        mock = Mock_Test(self.run_main, method, url, data, mock_response, header=None)
        mock.mock_test()
