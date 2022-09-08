# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 一马当先.py
@time: 2022/8/12 16:12
"""
n = 1
m = 2
direction = ([1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2,-1], [-2, 1], [-2, -1])
routine = [(0, 0)] #统计走过的格子
count = 0
temp_x, temp_y = 0, 0
while routine:
    now_x, now_y = routine.pop()
    if (now_x, now_y) == (m, n):
        break
    for x, y in direction:
        if (x, y) != (-temp_x, -temp_y):
            now_x += x
            now_y += y
            count += 1
            if now_x < 0 or now_x > m or now_y < 0 or now_y > n:
                count -= 1
                now_x -= x
                now_y -= y
                continue
            else:
                temp_x, temp_y = x, y
                routine.append((now_x, now_y))
                break
if (now_x, now_y) != (m, n):
    count = 0
if count != 0:
    print(count)
else:
    print(-1)