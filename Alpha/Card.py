#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 动态卡片类，包含动态的av号、名称、描述、时间、UP主、封面链接6类信息。
@Date: 2019-02-21
@LastEditTime: 2019-02-21
'''


class Card:
    def __init__(self, av, uname, citme, title, desc, cover):
        self.av = int(av)
        self.uname = uname
        self.desc = desc
        self.ctime = int(citme)
        self.title = title
        self.cover = cover

    # 比较函数，用于排序（根据时间）
    def __lt__(self, other):
        return self.ctime < other.ctime

    def __eq__(self, other):
        return self.ctime == other.ctime

    def __ge__(self, other):
        return self.ctime > other.ctime
