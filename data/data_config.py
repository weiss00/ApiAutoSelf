# -*- coding: utf-8 -*-

from tools.constant import Const

class Global_Var:
    """
        引入外部工具类，保证常量不可变
        处理excel表中， 将其表中每列变为静态变量
    """
    const = Const()
    const.ID = 0
    const.URL = 2
    const.REQUEST_METHOD = 3
    const.DEPEND_ID = 4
    const.DEPEND_DATA = 5
    const.DEPEND_DATA_NAME = 6
    const.HEADER = 7
    const.REQUEST_DATA = 8
    const.EXCEPT = 9
    const.DATA_TYPE = 10
    const.RUN = 11
    const.RESULT = 12

    # 获取case_id
    @classmethod
    def get_id(cls):
        return cls.const.ID

    # 获取url
    @classmethod
    def get_url(cls):
        return cls.const.URL

    # 获取请求方式
    @classmethod
    def get_request_method(cls):
        return cls.const.REQUEST_METHOD

    # 获取依赖id
    @classmethod
    def get_depend_id(cls):
        return cls.const.DEPEDN_ID

    # 获取依赖数据
    @classmethod
    def get_depend_data(cls):
        return cls.const.DEPEDN_DATA

    # 获取依赖数据的字段
    @classmethod
    def get_depend_data_name(cls):
        return cls.const.DEPEND_DATA_NAME

    # 获取请求头
    @classmethod
    def get_header(cls):
        return cls.const.HEADER

    # 获取请求数据
    @classmethod
    def get_request_data(cls):
        return cls.const.REQUEST_DATA

    # 获取预期结果
    @classmethod
    def get_except(cls):
        return cls.const.EXCEPT

    # 获取实际结果
    @classmethod
    def get_result(cls):
        return cls.const.RESULT

    # 获取传入数据类型
    @classmethod
    def get_data_type(cls):
        return cls.const.DATA_TYPE

    # 获取执行状态
    @classmethod
    def get_run(cls):
        return cls.const.RUN

    # 获取请求头header的值
    def get_header_value(self):
        header = {
            "header" : "123",
            "cookie" : "weiss133231"
        }
        return header

if __name__ == '__main__':
    # url = Global_Var.get_id()
    # run = Global_Var.get_run()
    print(Global_Var.get_header_value())