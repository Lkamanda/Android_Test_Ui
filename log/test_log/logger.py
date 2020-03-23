# @Description: 日志 生成mylogger实例
import logging
import time
from common.custom import *

class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.CRITICAL)
        rq = time.strftime("%Y-%m-%d -%H-%M", time.localtime((time.time())))

        # 生成日志文件

        log_name = get_root_directory() + gsb()+ 'mylog' + gsb() +"logs" + gsb() + rq + 'mylog.text'
        fh = logging.FileHandler(log_name, encoding='utf-8')
        # except:
        #     log_name = get_root_directory() + gsb()+ 'mylog' + gsb() + "logs" + gsb() + rq +'xx'+ 'mylog.text'
        #     fh = logging.FileHandler(log_name, encoding='utf-8')

        # 权重自上到下 10， 20， 30 ，40， 50
        fh.setLevel(logging.DEBUG)
        fh.setLevel(logging.INFO)
        fh.setLevel(logging.WARNING)
        fh.setLevel(logging.ERROR)
        fh.setLevel(logging.CRITICAL)

        # 创建一个handler用于控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setLevel(logging.INFO)
        ch.setLevel(logging.WARNING)
        ch.setLevel(logging.ERROR)
        ch.setLevel(logging.CRITICAL)
        #定义handler输出格式
        formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s -%(message)s")

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger 添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

mylogger = Logger(logger="Logger").get_log()




