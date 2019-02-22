#!python3
# -*- coding: utf-8 -*-

# 读入cookies配置信息，主要为登录信息
cookie = open("./cookies", "r").readline()

# 格式处理
cookie = cookie.replace(' ', '')
cookie = cookie.split(';')

COOKIES = {}

for i in cookie:
    name, value = i.split('=')
    COOKIES[name] = value
