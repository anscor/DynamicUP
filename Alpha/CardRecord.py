#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 记录最近一次更新的信息（按动态ID升序）
@Date: 2019-02-21
@LastEditTime: 2019-02-23
'''


import Card

import codecs
import json
import copy

__Card = Card.Card(av="-1", uname="", title="",
                   desc="", dynamic_id="-1", cover="")


# 从本地文件中读取最近一次更新的信息
f = codecs.open("./LastCard.json", "r", "utf-8")
c = json.load(f)
f.close()
__Card.av = int(c["av"])
__Card.uname = c["uname"]
__Card.title = c["title"]
__Card.desc = c["desc"]
__Card.dynamic_id = int(c["dynamic_id"])
__Card.cover = c["cover"]


# 获取最近一次更新的信息
def GetLastCard():
    return copy.deepcopy(__Card)


# 设置最近一次更新
def SetLastCard(card):
    __Card.av = card.av
    __Card.uname = card.uname
    __Card.title = card.title
    __Card.desc = card.desc
    __Card.dynamic_id = card.dynamic_id
    __Card.cover = card.cover
    __Record()


# 将最近一次更新的信息保存到本地文件中
def __Record():
    c = {}
    c["av"] = __Card.av
    c["uname"] = __Card.uname
    c["title"] = __Card.title
    c["desc"] = __Card.desc
    c["dynamic_id"] = __Card.dynamic_id
    c["cover"] = __Card.cover
    f = codecs.open("./LastCard.json", "w", "utf-8")
    json.dump(c, f)
    f.close()
