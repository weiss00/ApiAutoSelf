# -*- config: utf-8 -*-
"""
读取配置文件工具类  使用yaml方便操作
"""
import yaml

class ReadConfig(object):

    def __init__(self, keyword):
        self.filepath = "../config/config.yaml"
        self.keyword = keyword

    def read_config_keyword(self):
        with open(self.filepath, 'r') as f:
            self.config = yaml.load_all(f, Loader=yaml.FullLoader)
            for item in self.config:
                if item.get(self.keyword):
                    # print(item.get(self.keyword))
                    return item.get(self.keyword)

    def read_config(self):
        with open(self.filepath, 'r') as f:
            self.config = yaml.load_all(f, Loader=yaml.FullLoader)
            for item in self.config:
                return item


if __name__ == '__main__':
    c = ReadConfig("host")
    k = c.read_config()
    print(k)
