# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 时间就是金钱.py
@time: 2022/8/10 15:46
"""
st = "00:00:00"
et = "00:00:10"
s = [int(x) for x in st.split(':')]  # 从字符串中拆分出时、分、秒
e = [int(x) for x in et.split(':')]

diff = (e[0] * 60 * 60 + e[1] * 60 + e[2]) - (s[0] * 60 * 60 + s[1] * 60 + s[2])  # 计算两个时间的间隔（秒）
print(diff)
