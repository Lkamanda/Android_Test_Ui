# @Description:提供appium driver

from appium import webdriver
from log.logger import mylog
import os, time
from common.custom import get_deviceName,get_platformVersion

class MyDriver(object):
    # @classmethod
    # def setUpClass(cls):
    #     desire_caps={
    #         "deviceName":get_deviceName(),
    #         "platformName": "Android",
    #         "PlatfromVersion": get_platformVersion(),
    #         "appPackage":"com.ss.android.article.news",
    #         # "appPackage": "com.sogou.novel",
    #         "appActivity":"com.ss.android.article.news.activity.MainActivity",
    #         # "appActivity":"com.sogou.novel.home.SplashActivity",
    #         "noReset": True, # 是否重置app
    #         "unicodeKeyboard": True,
    #         "newCommandTimeout":"120",# 设置未接受命令超时时间，driver关闭时间
    #         # "autoLaunch":False # 是否自动启动app
    #     }
    #     try:
    #         cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
    #         mylog.logger.info('链接成功')
    #     except Exception as e:
    #         mylog.logger.error(e)
    #     cls.driver.implicitly_wait(10)
    #
    # # @classmethod
    # # def tearDownClass(cls):
    # #     cls.driver.quit()
    # #     mylog.logger.debug('driver关闭')


    def startUp(self):
        """
        链接app
        :return:
        """
        desire_caps = {
            "deviceName": get_deviceName(),
            "platformName": "Android",
            "PlatfromVersion": get_platformVersion(),
            "appPackage": "com.ss.android.article.news",
            # "appPackage": "com.sogou.novel",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            # "appActivity":"com.sogou.novel.home.SplashActivity",
            "noReset": True,  # 是否重置app
            "unicodeKeyboard": True,
            "newCommandTimeout": "120",  # 设置未接受命令超时时间，driver关闭时间
            # "autoLaunch":False # 是否自动启动app
        }
        try:
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            mylog.logger.info('链接成功')
        except Exception as e:
            mylog.logger.error(e)
        self.driver.implicitly_wait(10)
        return self.driver



