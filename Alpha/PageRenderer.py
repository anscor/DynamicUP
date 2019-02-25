#!python3
# -*- coding: utf-8 -*-
'''
@Author: Sion10032
@LastEditors: Sion10032
@Description: 渲染邮件html页面
@Date: 2019-02-25
@LastEditTime: 2019-02-25
'''

import Card
import Dynamic

class PageRenderer:

    def __init__(self):
        self.wrapper = open('./Templates/Wrapper.html', 'r', encoding='UTF-8').read()
        self.listItem = open('./Templates/ListItem.html', 'r', encoding='UTF-8').read()
        self.videoInfo = open('./Templates/VideoInfo.html', 'r', encoding='UTF-8').read()

    def Render(self, cards):
        result = self.wrapper
        listItems = ''

        cs = {}
        for card in cards:
            if not card.uname in cs:
                cs[card.uname] = []
            cs[card.uname].append(card)

        for key, value in cs.items():
            li = self.listItem
            li = li.replace('{ UPName }', key)

            vfs = ''
            for card in value:
                vfs = vfs + self.__RenderVideoInfo(card)
            li = li.replace('{ VideoInfo }', vfs)

            listItems = listItems + li

        result = result.replace('{ list-item }', listItems)

        return result

    def __RenderVideoInfo(self, card):
        vi = self.videoInfo

        vi = vi.replace('{ VideoLink }', 'https://www.bilibili.com/video/av' + str(card.av))
        vi = vi.replace('{ CoverImgSrc }', card.cover + '@160w_100h.webp')
        vi = vi.replace('{ VideoTitle }', card.title)
        vi = vi.replace('{ VideoDescription }', card.desc.replace('\n', '<br />'))

        return vi

if __name__ == '__main__':
    cs = Dynamic.ListUpdate()
    pr = PageRenderer()
    print(pr.Render(cs))