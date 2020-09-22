# -*- coding:utf-8 -*-
import json

import requests

"""
    简单封装get / post 基类
"""

class RunMethod(object):

    def post_main(self, url, data, header=None):
        res = None
        if header == None:
            res = requests.post(url=url, data=data)
        else:
            res = requests.post(url=url, data=data, headers=header)
        print(res.status_code)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header == None:
            res = requests.get(url=url, data=data)
        else:
            res = requests.get(url=url, data=data, headers=header)
        return res.json()

    def run_main(self, method, url, data, header):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True)
