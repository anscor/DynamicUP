#!python3
# -*- coding: utf-8 -*-
'''
@Author: Anscor
@LastEditors: Anscor
@Description: 主文件，整合所有模块
@Date: 2019-01-27
@LastEditTime: 2019-02-25
'''


import Mail
import Config

import time
import random

if __name__ == "__main__":
    while True:
        Mail.Send()
        time.sleep(random.randint(Config.MinTime, Config.MaxTime))
