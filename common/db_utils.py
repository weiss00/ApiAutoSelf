# -*- coding: utf-8 -*-
"""
工具类---关于数据库配置查询简单封装
"""
import pymysql
from common.read_config import ReadConfig
from loguru import logger

class DB_Utils(object):

    # logger.info(lists)
    # 初始化db连接
    def __init__(self):
        host, user, password, port, database = [v for k, v in ReadConfig("host").read_config().items()]
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=int(port),
            database=database
        )
        self.cursor = self.conn.cursor()

    def select_item(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            logger.info(f'{result}, {type(result[0])}')
            return result[0]
        except Exception as e:
            logger.info(f'{e}')
        finally:
            self.cursor.close()
            self.conn.close()


if __name__ == '__main__':
    db = DB_Utils()
    sql = "select code from users_verifycode where mobile = '18844077779';"
    db.select_item(sql)