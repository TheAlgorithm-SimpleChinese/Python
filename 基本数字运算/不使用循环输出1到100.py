# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 不使用循环输出1到100.py
@time: 2022/6/14 16:28
"""


def prints(n):
    if n > 0:
        prints(n - 1)
        print(str(n))


def main():
    prints(100)


if __name__ == "__main__":
    main()
