#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 项目配置文件，包含发送方用户邮件配置、请求API相关配置、调试配置等
@Date: 2019-02-21
@LastEditTime: 2019-02-22
'''


import Cookie

# 调试
DEBUG = False

# 用户信息
USER = ""
PASSWORD = ""
TO_ADDR = ""
FROM_ADDR = ""
HOST = ""

# 请求API信息
URL = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=15047663&type=8"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Host": "api.vc.bilibili.com",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive"
}
COOKIE = Cookie.COOKIES
