#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 项目配置文件，包含发送方用户邮件配置、请求API相关配置、调试配置等
@Date: 2019-02-21
@LastEditTime: 2019-02-25
'''


# 调试
DEBUG = False

# ----------时间间隔----------
# 最小刷新时间
MinTime = 173
# 最大刷新时间
MaxTime = 352
# ----------时间间隔----------

# ----------用户信息----------
# 用户邮箱账号
USER = ""
# 账号密码
PASSWORD = ""
# 收件人
TO_ADDR = ""
# 发件人
FROM_ADDR = ""
# 邮箱服务器地址（SMTP）
HOST = ""
# 用户B站UID
UID = ""
# ----------用户信息----------

# ----------请求API信息----------
# cookie信息
COOKIE = {
    "l": "",
    "LIVE_BUVID": "",
    "SESSDATA": ""
}

URL = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=%s&type=8" % UID
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
# ----------请求API信息----------
