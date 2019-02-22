#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 获取动态并对动态进行处理，提取其中需要信息，将其转换为list结构并返回
@Date: 2019-02-21
@LastEditTime: 2019-02-21
'''


import json
import Card
import config
import CardRecord

import requests


def __GetOriginalDynamic():

    # 设置url
    url = config.URL

    # 设置Cookie
    cookies = config.COOKIE

    # 设置请求头
    headers = config.HEADERS

    # 请求动态
    req = requests.get(url=url, cookies=cookies, headers=headers)
    req.encoding = "utf-8"
    dynamic = req.text

    if config.DEBUG == True:
        # 将返回的动态信息（json格式）写入文件
        with open("./dynamic.json", "w", encoding="utf-8") as f:
            f.write(dynamic)
        f.close()
        print("成功获取到动态")
    else:
        return dynamic


def ListUpdate():
    if config.DEBUG == True:
        # 读入动态信息
        f = open("./dynamic.json", "r", encoding="utf-8")
        # 将json转换成字典
        jsonData = json.load(f)
        f.close()
    else:
        jsonData = json.loads(__GetOriginalDynamic())

    cards = []
    if jsonData["code"] != 0:
        return cards
    # 获取动态
    dynamics = jsonData["data"]["cards"]
    # 从动态中提取所需信息
    for dynamic in dynamics:
        # av号
        av = dynamic["desc"]["rid"]
        # UP主
        uname = dynamic["desc"]["user_profile"]["info"]["uname"]

        d = json.loads(dynamic["card"])
        # 更新时间
        ctime = d["ctime"]
        # 标题
        title = d["title"]
        # 描述
        desc = d["desc"]
        # 封面链接（全尺寸原图）
        cover = d["pic"]

        card = Card.Card(av=av, uname=uname, title=title,
                    desc=desc, citme=ctime, cover=cover)
        cards.append(card)

    # 将获取的动态按时间进行升序排序
    cards = sorted(cards)

    # 获取最新一次更新的信息
    last = CardRecord.GetLastCard()
    
    # 从动态中找出所有的更新
    i = 0
    while True:
        if cards[i] > last:
            break
        i = i + 1
        if i == len(cards):
            break

    # 设置最新一次更新
    CardRecord.SetLastCard(cards[len(cards) - 1])

    if last.ctime == -1 or i == len(cards):
        cards = []
    else:
        cards = cards[i:]
    return cards
