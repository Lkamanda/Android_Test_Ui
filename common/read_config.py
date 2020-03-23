# @Time       :      2020/3/21 13:51
# @Description: 配置文件读取
import configparser
from common.custom import get_root_directory
import os


class ReadConfig(object):

    def __init__(self):
        self.configP = 'config.ini'
        self.configPath = os.path.join(get_root_directory(), self.configP)
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configPath, encoding="utf-8")

    def get_config_email(self, name):
        # 获取去config.ini中的 [email]下的字段信息
        name = self.cf.get('email', name)
        return name

    def get_config_mysql(self, name):
        # 获取config.ini 中的 [mysql]下的字段信息
        name = self.cf.get('mysql', name)


if __name__ == '__main__':
    con = ReadConfig()
    print(con.get_config_email('mail_host'))
