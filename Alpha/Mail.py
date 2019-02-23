#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 邮件发送
@Date: 2019-02-21
@LastEditTime: 2019-02-23
'''


import config
import Dynamic

import smtplib
from email.utils import formataddr, parseaddr
from email.mime.text import MIMEText
from email.header import Header

import codecs


def __format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 构造HTML界面
def __CreateHTML(cards):
    
    html = '<!DOCTYPE html><html><head><meta charset="utf-8"/></head><body style = "width: 800px"><ul>'

    up = ""
    li = ''
    c = ''
    for card in cards:
        li = ''
        if card.uname != up:
            if up != "":
                li = li + '</div></li>'
            up = card.uname
            html = html + li

            li = '<li><div><h3>%s</h3>' % card.uname
        
        c = '<div style="height:100px;width:800px;margin:20px 0px">'
        c = c + '<div style="float:left;height:100px;">'
        c = c + '<a href="https://www.bilibili.com/video/av%s/"><img src="%s@160w_100h.webp"/></a>' % (card.av, card.cover)
        c = c + '</div>'
        c = c + '<div style="float:left;height:100px;width:600px;overflow:hidden;margin-left:10px">'
        c = c + '<div><b>%s</b></div>' % card.title
        c = c + '<div style="margin-top: 10px;">'
        c = c + card.desc.replace("\n", "<br />")
        c = c + '</div></div></div>'
        
        li = li + c
        html = html + li

    html = html + '</div></li></ul></body></html>'
    return html

def Send():
    user = config.USER
    password = config.PASSWORD
    to_addr = config.TO_ADDR
    from_addr = config.FROM_ADDR
    host = config.HOST

    sbj = "[BilibiliUP]"

    # 获取所有有更新的UP主，并添加到主题中
    cards = Dynamic.ListUpdate()
    # 没有更新时不发送
    if len(cards) == 0:
        if config.DEBUG == True:
            print("没有更新")
        return
    for card in cards:
        if sbj.find(card.uname) == -1:
            sbj = sbj + ' ' + card.uname

    # 构建发送内容与头部
    msg = MIMEText(__CreateHTML(cards), "html", "utf-8")
    msg['From'] = __format_addr("BilibiliUP<xlyAnge1@163.com>")
    msg['To'] = __format_addr("Anscor<xlyanscor@outlook.com>")
    msg['Subject'] = Header(sbj, "utf-8").encode()

    # 发送
    server = smtplib.SMTP(host, 25)
    if config.DEBUG == True:
        server.set_debuglevel(True)
    server.login(user, password)
    server.sendmail(from_addr, [from_addr, to_addr], msg.as_string())
    server.quit()
