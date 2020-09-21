# -*- config: utf-8 -*-
"""
读取配置文件工具类  使用yaml方便操作
"""
import yaml

class ReadConfig(object):

    def __init__(self):
        self.filepath = "../config/config.yaml"
        # self.keyword = keyword

    def read_config_keyword(self, keyword):
        with open(self.filepath, 'r') as f:
            self.config = yaml.load_all(f, Loader=yaml.FullLoader)
            for item in self.config:
                if item.get(keyword):
                    # print(item.get(self.keyword))
                    return item.get(keyword)

    def read_config_items(self):
        with open(self.filepath, 'r') as f:
            self.config = yaml.load_all(f, Loader=yaml.FullLoader)
            for item in self.config:
                return item


if __name__ == '__main__':
    c = ReadConfig("host")
    k = c.read_config()
    print(k)
