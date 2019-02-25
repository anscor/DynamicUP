#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 获取动态并对动态进行处理，提取其中需要信息，将其转换为list结构并返回
@Date: 2019-02-21
@LastEditTime: 2019-02-25
'''


import json
import Card
import Config
import CardRecord

import requests


def __GetOriginalDynamic():

    # 设置url
    url = Config.URL

    # 设置Cookie
    cookies = Config.COOKIE

    # 设置请求头
    headers = Config.HEADERS

    # 请求动态
    req = requests.get(url=url, cookies=cookies, headers=headers)
    req.encoding = "utf-8"
    dynamic = req.text

    if Config.DEBUG == True:
        # 将返回的动态信息（json格式）写入文件
        with open("./dynamic.json", "w", encoding="utf-8") as f:
            f.write(dynamic)
        f.close()
        print("成功获取到动态")
    return dynamic


def ListUpdate():
    # if Config.DEBUG == True:
    #     # 读入动态信息
    #     f = open("./dynamic.json", "r", encoding="utf-8")
    #     # 将json转换成字典
    #     jsonData = json.load(f)
    #     f.close()
    # else:
    #     jsonData = json.loads(__GetOriginalDynamic())
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
        # 动态ID
        dynamic_id = dynamic["desc"]["dynamic_id"]
        # UP主
        uname = dynamic["desc"]["user_profile"]["info"]["uname"]

        d = json.loads(dynamic["card"])
        # 标题
        title = d["title"]
        # 描述
        desc = d["desc"]
        # 封面链接（全尺寸原图）
        cover = d["pic"]

        card = Card.Card(av=av, uname=uname, title=title,
                    desc=desc, dynamic_id=dynamic_id, cover=cover)
        cards.append(card)

    # 将获取的动态按动态ID进行升序排序
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

    if last.dynamic_id == -1 or i == len(cards):
        cards = []
    else:
        cards = cards[i:]
    return cards
