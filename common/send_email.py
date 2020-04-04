import smtplib
import time
import os
from email.mime.text import MIMEText
from common.read_config import ReadConfig
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from log.logger import mylog


def send_mail_html(email_dir):
    '''发送html内容邮件，非附件形式，即直接在邮件中显示html'''
    readC = ReadConfig()
    sender = readC.get_config_email('sender')
    receiver = readC.get_config_email('receiver')
    content = readC.get_config_email('content')
    # 发送邮件主题
    t = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    subject = '接口自动化测试结果_' + t

    # 使用smtp服务
    smtpserver = readC.get_config_email('mail_host')

    mail_user = readC.get_config_email('mail_user')

    mail_pass = readC.get_config_email('mail_pass')

    # 开始打包邮件
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject



    # 邮件 内容content
    pureText = MIMEText(content, 'html', 'utf-8')
    msg.attach(pureText)

    file_path, file_name = find_new_file(dir=email_dir)
    file = r"{}".format(file_path)
    # 添加邮件附件
    att = MIMEApplication(open(file, 'rb').read())
    # att.add_header('Content-Disposition', 'p_w_upload', file_name='interfaceReport.html')
    att.add_header('Content-Disposition', 'p_w_upload', filename=file_name)
    msg.attach(att)
    try:
        server = smtplib.SMTP(smtpserver)
        server.login(mail_user, mail_pass)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        mylog.logger.debug('邮件发送成功')
    except Exception as e:
        mylog.logger.debug('邮件发送失败%s'%e)


def find_new_file(dir):
    # 将指定目录下文件添加到一个列表中返回
    file_lists = os.listdir(dir)
    # print(file_lists)
    # os.get.getatime(file)返回文件的最后修改时间
    # os.path.isdire(file) 判断file 是否为路径， 返回true， false
    file_lists.sort(key=lambda fn: os.path.getatime(dir + "\\" + fn) if not os.path.isdir(dir +"\\"+ fn)else 0)
    # print(file_lists)
    file_name = file_lists[-1]
    file_path = os.path.join(dir, file_name)
    mylog.logger.info(file_lists[-1])
    return file_path, file_name


if __name__ == '__main__':
    dir = r"C:\Users\15992\PythonProject\Android_Test_Ui\testReport"

    send_mail_html(dir)


















