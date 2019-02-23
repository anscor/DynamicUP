#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 处理Cookie文件
@Date: 2019-02-23
@LastEditTime: 2019-02-23
'''


import json

# 读入cookies配置信息，主要为登录信息
cookie = open("./cookies", "r").readline()

# 格式处理
cookie = cookie.replace(' ', '')
cookie = cookie.split(';')

COOKIES = {}

for i in cookie:
    name, value = i.split('=')
    COOKIES[name] = value


