# @Time       :      2020/3/22 12:13
# @Description: 初始化环境和生成关闭driver
import unittest
from common.Driver import MyDriver
from log.logger import mylog

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mydriver = MyDriver()
        cls.driver = mydriver.startUp()
        mylog.logger.debug("整个测试类初始化完成")

    def setUp(self):
        self.driver.launch_app()
        mylog.logger.debug('每个测试用例初始化')

    def tearDown(self):
        self.driver.close_app()
        mylog.logger.debug('每个测试用列结束清楚环境')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        mylog.logger.debug('整个测试类清楚环境')


