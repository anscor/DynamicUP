#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 邮件发送
@Date: 2019-02-21
@LastEditTime: 2019-02-25
'''


import Config
import Dynamic
import PageRenderer

import smtplib
from email.utils import formataddr, parseaddr
from email.mime.text import MIMEText
from email.header import Header

import codecs


def __format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def Send():
    user = Config.USER
    password = Config.PASSWORD
    to_addr = Config.TO_ADDR
    from_addr = Config.FROM_ADDR
    host = Config.HOST

    sbj = "[BilibiliUP]"

    # 获取所有有更新的UP主，并添加到主题中
    cards = Dynamic.ListUpdate()
    # 没有更新时不发送
    if len(cards) == 0:
        if Config.DEBUG == True:
            print("没有更新")
        return
    for card in cards:
        if sbj.find(card.uname) == -1:
            sbj = sbj + ' ' + card.uname

    page = PageRenderer()

    # 构建发送内容与头部
    msg = MIMEText(page.Render(cards), "html", "utf-8")
    msg['From'] = __format_addr("BilibiliUP<xlyAnge1@163.com>")
    msg['To'] = __format_addr("Anscor<xlyanscor@outlook.com>")
    msg['Subject'] = Header(sbj, "utf-8").encode()

    # 发送
    server = smtplib.SMTP(host, 25)
    if Config.DEBUG == True:
        server.set_debuglevel(True)
    server.login(user, password)
    server.sendmail(from_addr, [from_addr, to_addr], msg.as_string())
    server.quit()
