# @Time       :      2020/3/17 0:21
# @Description: 一些自定义关于系统的方法

import os
import platform
import re


# 获取当前的根目录
def get_root_directory():
    path = os.path.dirname(os.path.dirname(__file__))
    return path


# 判断当前系统
def getSysterm():
   return platform.system()


# 根据当前系统判断 \ /  getPathSymbol
def gsb():
    if getSysterm() == "Windows":
        return '/'
    else:
        return '\\'


# 获取链接手机的devices
def get_deviceName():
    readDeviceId = list(os.popen('adb devices').readlines())
    # 正则表达式匹配出 id 信息
    # ['List of devices attached\n', '245576a2\tdevice\n', '\n']
    deviceName = re.findall(r'^\w*\b', readDeviceId[1])[0]
    # mylog.logger.debug("deviceName：%s" %deviceName)
    return deviceName

# 获取手机的android版本
def get_platformVersion():
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
    # mylog.logger.debug("platformVersion:%s"%platformVersion)
    return platformVersion



