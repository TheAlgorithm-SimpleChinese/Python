# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 田忌赛马.py
@time: 2022/11/7 20:19
"""
la = [92, 83, 71]
lb = [95, 87, 74]
lb.sort(reverse=True)
dp = []
count = 0
for i in range(len(lb)):
    if max(la) >= lb[i]:
        count = count + 200 if max(la) > lb[i] else count
        dp.append(max(la))
        la.remove(max(la))
    else:
        dp.append(min(la))
        la.remove(min(la))
        count -= 200
print(count)
