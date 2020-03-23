# @Time       :      2020/3/18 3:30
# @Description: TestHome测试用例类


from log.logger import mylog
from testSuit.element_object.element import Element
import time
import unittest
from common.read_excal import ReadExcal
from ddt import ddt, data

@ddt
class TestHome(Element):
    @unittest.skip
    def test_xl(self):
        self.get_id("com.ss.android.article.news:id/byg").click()
        mylog.logger.info('第一条测试用例')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("发微头条")').click()

        # self.press_keycode(24)
        self.get_text("发微头条").click()
        # self.get_id("com.ss.android.article.news:id/a8j").send_keys('测试')
        # self.get_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
        #                "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.bytedance.android.gaia.activity.slideback.SlideFrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/"
        #                "android.widget.RelativeLayout/android.widget.TextView[3]").click()
        # self.set_network(2)


    @data(1,2,3,4,5,6,7)
    def test_search(self,a):
        print(self._testMethodName) # 方法名
        print(self.__class__.__name__) # 类名
        readExcal = ReadExcal()
        text = readExcal.get_content(
            className=self.__class__.__name__,
            methodName=self._testMethodName,
            x=0
        )

        self.get_id('com.ss.android.article.news:id/crq').click()
        self.get_id('com.ss.android.article.news:id/csp').send_keys(text)
        self.get_id('com.ss.android.article.news:id/cm6').click()
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()