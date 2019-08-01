#! /usr/bin/env python
# coding:utf-8
"""
Author: zhiying
Date: 2019.8.1
URl: www.zhouzying.cn
Description: 关注志颖博客(www.zhouzying.cn),一起探讨爬虫技术！
"""
import math
import time
import datetime


def countdown():
    # math.trunc()是取整函数
    nowtime = math.trunc(time.time())
    # 结束时间为:2019-12-21 09:00:00
    # 将时间转化成时间戳
    endtime = time.mktime(datetime.datetime(2019, 12, 21, 9, 0, 0).timetuple())
    delta_time = endtime - nowtime
    # 天
    d = delta_time // 3600 // 24
    # 时
    h = delta_time // 3600 % 24
    # 分
    m = delta_time // 60 % 60
    # 秒
    s = delta_time % 60
    print('今天距离2020年考研还有:{}天{}小时{}分{}秒'.format(math.trunc(d), math.trunc(h), math.trunc(m), math.trunc(s)))


"""
def countdown2():
    nowtime = math.trunc(time.time())
    # 结束时间为:2019-12-21 09:00:00
    endtime = time.mktime(datetime.datetime(2019, 12, 21, 9, 0, 0).timetuple())
    delta_time = endtime - nowtime
    # 天
    d = delta_time // 3600 // 24
    # 时
    h = (delta_time - d * 24 * 3600) // 3600
    # 分
    m = (delta_time - d * 24 * 3600 - h * 3600) // 60
    # 秒
    s = (delta_time - d * 24 * 3600 - h * 3600 - m * 60)
    print('今天距离2020年考研还有:{}天{}小时{}分{}秒\n'.format(math.trunc(d), math.trunc(h), math.trunc(m), math.trunc(s)))
    """
if __name__ == '__main__':
    countdown()
