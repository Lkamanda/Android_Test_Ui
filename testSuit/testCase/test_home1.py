# @Time       :      2020/3/18 3:30
# @Description: TestHome测试用例类

from log.logger import mylog
from testSuit.po.element import Element
import time
import unittest
from common.read_excal import ReadExcal
from ddt import ddt, data
from common.my_test import MyTest

from testSuit.po.HomePage import HomePage
class TestHome(MyTest):

    def test_w(self):
        hp = HomePage(self.driver)
        time.sleep(4)
        hp.clickPublishButton()
        hp.clickWeiTouTiao()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()