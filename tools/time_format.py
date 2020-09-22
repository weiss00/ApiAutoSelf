# -*- coding:utf-8 -*-

import time
from loguru import logger

"""
    工具类: 格式化时间
"""

class Time_Format(object):

    @classmethod
    def format_time(cls):
        time_format = time.strftime('%Y%m%d-%H%M%S', time.localtime())
        # logger.info(f"format-time is {time_format}")
        return time_format

if __name__ == '__main__':
    Time_Format.format_time()