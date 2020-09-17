# -*- coding: utf-8 -*-
"""
思路： 利用注册成功  / 登陆获取token 并设置为全局变量   携带后访问需要用户验证的操作
获取token
"""

from api.send_request import BaseRequest

class Get_Token(object):

    def __init__(self):
        BaseRequest().base_requests()

    def get_token(self):
        pass


