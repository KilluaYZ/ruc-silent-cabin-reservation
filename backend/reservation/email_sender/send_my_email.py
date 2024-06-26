# clriocahxwmsdcfg
# IMAP/SMTP 设置方法
# 用户名/帐户： 你的QQ邮箱完整的地址
# 密码： 生成的授权码
# 电子邮件地址： 你的QQ邮箱的完整邮件地址
# 接收邮件服务器： imap.qq.com，使用SSL，端口号993
# 发送邮件服务器： smtp.qq.com，使用SSL，端口号465或587

import smtplib
from email.mime.text import MIMEText #邮箱正文
from email.mime.multipart import MIMEMultipart #邮箱主体
from email.header import Header #邮箱头、标题、收件人
import config
from reservation.email_sender.email_htmls import getRegisterEmail, getChangePasswdEmail
from flask import current_app

# mail_host = current_app.config['MAIL_HOST']
# mail_user = current_app.config['MAIL_USER']
# mail_pass = current_app.config['MAIL_PASSWORD']
# sender = current_app.config['MAIL_SENDER']
# title = current_app.config['MAIL_TITLE']

mail_host = config.MAIL_HOST
mail_user = config.MAIL_USER
mail_pass = config.MAIL_PASSWORD
sender = config.MAIL_SENDER
title = config.MAIL_TITLE
info_title = config.MAIL_INFO_TITLE
def sendEmail(mail_title: str, mail_content: str, mail_receiver: str, mail_type='html'):
    msg = MIMEMultipart()
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['From'] = sender
    if mail_type == 'html':
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    elif mail_type == 'plain':
        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, mail_receiver, msg.as_string())
        smtpObj.quit()
        print(f'向{mail_user}发送邮件成功')
    except smtplib.SMTPException as e:
        print(f'Error: 无法向{mail_user}发送邮件')
        print(e)

def sendRegisterEmail(userName: str, checkCode: str, mail_receiver: str):
    sendEmail(title, getRegisterEmail(userName, checkCode), mail_receiver)

def sendChangePasswdEmail(userName: str, checkCode: str, mail_receiver: str):
    sendEmail(title, getChangePasswdEmail(userName, checkCode), mail_receiver)

def sendTextEmail(msg: str, mail_receiver: str):
    sendEmail(info_title, msg, mail_receiver, 'plain')
#
# sendRegisterEmail('ziyang','57736','2020201694@ruc.edu.cn')
# sendChangePasswdEmail('ziyang','57736','2020201694@ruc.edu.cn')

