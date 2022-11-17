# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: list深度.py
@time: 2022/11/17 23:21
"""
L = [1, 2, 3, [4, [5, 6]]]


def get_res(L):
    L = str(L)
    op_stack = []  # 临时
    op_stack_len = []  # 记录深度
    for i in L:
        if i == '[':
            op_stack.append(i)
            op_stack_len.append(len(op_stack))
        elif i == ']':
            op_stack.pop()
            op_stack_len.append(len(op_stack))
        else:
            pass
    return max(op_stack_len)


print(get_res(L))
