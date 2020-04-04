# @Time       :      2020/4/4 10:41
# @Description: 实现每个页面对象，将页面元素定义成类属性，元素的操作方法定义成发发
from testSuit.po.element import Element
from selenium.webdriver.common.by import By


class HomePage(Element):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.text = '发微头条'
        self.publish_botton = (By.ID,"com.ss.android.article.news:id/byw")

    def clickPublishButton(self):
        self.driver.find_element(*self.publish_botton).click()

    def clickWeiTouTiao(self):
        self.get_text(self.text).click()


