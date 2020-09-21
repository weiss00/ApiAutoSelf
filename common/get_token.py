# -*- coding: utf-8 -*-
"""
思路： 利用注册成功  / 登陆获取token 并设置为全局变量   携带后访问需要用户验证的操作
获取token
"""

class Get_Token(object):

    token = ""

    @classmethod
    def get_header(self, token):
        Get_Token.token =  {
            "Authorization": "JWT " + token
        }
        return Get_Token.token


if __name__ == '__main__':
    print(Get_Token.token + "==")
    print(Get_Token.get_header("333"))
    print(Get_Token.token)

