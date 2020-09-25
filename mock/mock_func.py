# -*- coding:utf-8 -*-

# import mock
from unittest.mock import Mock

# 模拟mock封装
class Mock_Test(object):

    def __init__(self, mock_method, method, url, request_data, response_data, header=None):
        """
        :param mock_method: mock的方法
        :param request_data:  请求的数据
        :param url: 请求的url
        :param method: 请求方式
        :param response_data: 响应数据
        :return:
        """
        # 返回数据
        self.mock_method = Mock(return_value=response_data)
        self.request_data = request_data
        self.url = url
        self.method = method
        self.header = header

    def mock_test(self):
        # 返回数据
        res = self.mock_method(self.method, self.url, self.request_data, self.header)
        return res