# Android_Test_Ui
基于python的androidUi自动化测试框架
- 环境搭建
    - 1.安装jdk，配置环境变量
    - 2.安装android sdk：SDK Manager 工具下载：Tools里前三个，extras里全勾
    - 3.安装Node.js
    - 4.安装.net framework
    - 5.安装appium,环境变量配置： xx\Appium\node_modules\.bin  添加到path中
    - 6.appium - python -client 下载 
    - 7.下载appium-desktop,链接真机/模拟器，用其获取app页面元素信息

- adb 
    - 1.adb devices 获取链接设备信息
    - 2.adb connect 127.0.0.1:port 用于连接模拟器
    - 3.获取 appPackage：aapt dump badging xx.apk |findstr package
        获取 appActivity:aapt dump badging xx.apk |findstr package (launchaable -activity)
      
- 框架结构：
    - bin：
        - runall：整个框架的启动文件
    - common：
        - custom：自定义方法
        - Driver：封装提供链接手机的Driver
        - HTMLTestRunner_PY3.py：HTML测试包模板包
        - read_config:读取配置文件
        - send_email:发送邮件
    - log：
        - logs:存放日志文件
        - logger.py: 提供日志类实例mylog，log.logger.info("日志信息")
    - testsuit：
        - element_object
            - element.py:对常用的定位页面元素方法进行二次封装
        - testcase:测试集
    - testdata：测试数据
    - testreport：测试报告存放位置
    - config.txt：配置文件
    
 
self._testMethodName) # 获取函数方法名 ， 只能在unittest下使用
self.__class__.__name__) # 类名
