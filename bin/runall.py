# @Description:整个自动化框架的启动文件
from common.HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
from common.custom import gsb
import os, time
from common.send_email import send_mail_html


class Runner(object):
    def __init__(self):
        self.gsb = gsb()
        self.gPath = os.path.dirname(os.path.dirname(__file__))
        self.testCase_root = '{0}{1}testSuit{1}testCase{1}'.format(self.gPath, self.gsb)
        #print(self.testCase_root)
        self.testReport_root = '{0}{1}testReport{1}'.format(self.gPath, self.gsb)
        #print(self.testReport_root)
        self.log_root = '{0}{1}log{1}logs{1}'.format(self.gPath, self.gsb)
        #print(self.log_root)

    def get_suit(self):
        suit = unittest.TestLoader().discover(
            start_dir=self.testCase_root,
            pattern="test*",
            top_level_dir=None,
        )
        return suit

    def my_run(self):
        report_path = os.path.join(self.testReport_root, '{}Testreport.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")))
        fp = open(report_path, 'wb')
        runner = HTMLTestRunner(
            stream=fp,
            title='test report',
            description='自动化测试报告'
        )
        suit= self.get_suit()
        runner.run(suit)
        # send email
        # send_mail_html(self.testReport_root)


if __name__ == '__main__':
    run = Runner()
    # print(time.strftime("%Y-%m-%d %H-%M-%S"))
    run.my_run()
