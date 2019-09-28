# encoding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header 
import time


class Send_Email(object):

    def __init__(self, receivers):

        self.mail_server = "smtp.qq.com"
        self.mail_port = 465
        self.sender = "aimingzhong@foxmail.com"
        self.sender_password = "glynjecffookbjff"  # 授权码
        self.receivers = receivers

    def send_info(self, mainText, subject):

        self.message = MIMEText(mainText, 'plain', 'utf-8')
        self.message['From'] = "aimingzhong@foxmail.com"
        self.message['To'] = self.receivers
        self.subject = Header(subject, 'utf-8')
        self.message['Subject'] = self.subject

        try:
            smtp_obj = smtplib.SMTP_SSL(self.mail_server,self.mail_port) 
            smtp_obj.login(self.sender, self.sender_password)
            smtp_obj.sendmail(self.sender, [self.receivers], self.message.as_string())
            print('send email success!')
        except smtp_obj.SMTPException as e:
            print('send email failure!')
            print(e)
        finally:
            smtp_obj.quit()