# -*- coding:utf-8 -*-

from common.operation_excel import Operation_Excel

class Is_Contain(object):

    def __init__(self):
        self.opera_excel = Operation_Excel()


    def is_contain(self, str_1, str_2):
        """
        :param str_1: 查找的字符串
        :param str_2:  被查找的字符串
        :return:
        """
        flag = None
        if str_1 in str_2:
            flag = True
        else:
            flag = False
        return flag
