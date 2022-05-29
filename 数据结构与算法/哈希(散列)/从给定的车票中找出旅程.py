# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 从给定的车票中找出旅程.py
@time: 2022/5/29 22:02
"""
"""
程序功能：从给定的车票中找出旅程
"""


def printResult(rout):
    # 用来存储把rout的键与值调换后的信息
    reverseInput = dict()
    for k, v in rout.items():
        reverseInput[v] = k
    start = None
    # 找到起点
    for k, v in rout.items():
        if k not in reverseInput:
            start = k
            break
    if start is None:
        print("输入不合理")
        return
    # 从起点出发按照顺序遍历路径
    to = rout[start]
    print(start + "->" + to, end=" ")
    start = to
    to = rout[to]
    while to is not None:
        print("  " + start + "->" + to, end=" ")
        start = to
        """
        使用下面这句会报错，get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。
        dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常。
        """
        # to = rout[to]
        to = rout.get(to)


def main():
    rout = dict()
    rout["西安"] = "成都"
    rout["北京"] = "上海"
    rout["大连"] = "西安"
    rout["上海"] = "大连"
    printResult(rout)


if __name__ == "__main__":
    main()
