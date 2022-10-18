# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: IP判断.py
@time: 2022/10/18 21:18
"""
s = "202.115.32.24"
b = 0
for each in s.split(sep="."):
    if each == "" or (each[0] == "0" and len(each) != 1) or not each.isdigit():  # 排除不到四位、开头等于0和不全是数字的情况
        b = 0
    break
if 0 <= int(each) < 256:
    b += 1
print("Yes" if b == 4 else "No")
