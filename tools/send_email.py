# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

class Send_Email(object):

    global send_user
    global host
    global password

    host = "smtp.163.com"
    send_user = "lihaiyi_weiss@163.com"
    password = "Lihaiyi1216"
    def send_email(self, user_list, sub, content):
        user = "weiss" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(host=host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

if __name__ == '__main__':
    send = Send_Email()
    user_list = ["1318714789@qq.com"]
    send.send_email(user_list, "测试邮件", "第一封测试邮件")