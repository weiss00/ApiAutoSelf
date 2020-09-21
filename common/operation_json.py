# -*- coding: utf-8 -*-

import json
from common.read_config import ReadConfig
from loguru import logger

class Operation_Json(object):
    """
    对excel中的依赖数据进行处理，提出到json文件中 便于操作
    """

    def __init__(self):
        self.json_path = ReadConfig().read_config_keyword("json_path")
        # print(self.json_path)

    def get_data(self, keyword=None):
        try:
            with open(self.json_path) as f:
                data = json.load(f)[keyword]
                # print(data)
                if data == None:
                    raise Exception("读取数据有误")
                else:
                    return data
        except Exception as e:
            logger.error(f"读取文件出错====>{e}")


if __name__ == '__main__':
    login_data = Operation_Json().get_data("addcart")
    logger.info(f"data is {login_data}, type is {type(login_data)}")
