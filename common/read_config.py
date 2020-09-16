# -*- config: utf-8 -*-
"""
读取配置文件工具类  使用yaml方便操作
"""
import yaml
from loguru import logger

class ReadConfig(object):

    def __init__(self, keyword):
        self.filepath = "../config/config.yaml"
        self.keyword = keyword

    def read_config(self):
        with open(self.filepath, 'r') as f:
            self.config = yaml.load_all(f, Loader=yaml.FullLoader)
            for item in self.config:
                if item.get(self.keyword):
                    # logger.info(f'{item.get("excel_path")}')
                    # print(item)
                    return item

if __name__ == '__main__':
    c = ReadConfig("excel_path")
    c.read_config()
