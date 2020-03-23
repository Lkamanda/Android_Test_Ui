# @Time       :      2020/3/22 10:51
# @Description: 连接mysql生成db对象

import pymysql

class ConnectMysql():

    def __init__(self):
        self.db = pymysql.connect(

        )