# @Time       :      2020/3/22 10:51
# @Description: 连接mysql生成db对象

import pymysql

class ConnectMysql():

    def __init__(self):
        try:
            self.db = pymysql.connect(
                host='192.168.0.113',
                user='root',
                password='123456',
                db='test1',
                port=3306
            )

        except Exception as e:
            print (e)

if __name__ == '__main__':
    con = ConnectMysql()

