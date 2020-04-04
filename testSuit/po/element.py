# @Time       :      2020/3/19 21:57
# @Description: 封装定为页面元素

from appium.webdriver.common.touch_action import TouchAction

class Element(object):

    def __init__(self, driver):
        self.driver =driver

    def get_id(self, id):
        #根据id地位页面元素
        return self.driver.find_element_by_id(id)

    def get_xpath(self,xpath):
        #根据xpath定位页面元素
        return self.driver.find_element_by_xpath(xpath)

    def get_text(self,text):
        #根据文本内容地位页面
        return self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("{}")'.format(text))

    def get_name(self, name):
        # 根据name定位页面元素
        return self.driver.find_element_by_name(name)

    def back(self):
        #返回按键
        self.driver.keyevent(4)

    def press_keycode(self, AndroidKeyCode):
        """
        android 系统按键
        :param AndroidKeyCode:
        home: 3,
        back:4,
        拨号：5，
        挂机：6，
        音量加：24，
        音量减少：25
        menu:82

        """
        return self.driver.press_keycode(AndroidKeyCode)

    # 未能调通
    def set_network(self, bitmask):
        # 设置网络
        return self.driver.set_network_connection(bitmask)

    def action_func(self):
        """
        action.xx

        :return: action 对象
        """
        action = TouchAction(self.driver)
        return action


    # driver.contexts 获取所有上下文
    # driver.current_context  获取当前上下文
    # driver.shake 摇晃设备