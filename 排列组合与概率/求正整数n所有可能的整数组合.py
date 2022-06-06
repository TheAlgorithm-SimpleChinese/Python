# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求正整数n所有可能的整数组合.py
@time: 2022/6/6 13:13
"""
"""
方法功能：求和为sums的所有整数组合
输入参数：sums正整数，result存储组合结果,count记录组合中数字的个数
"""


def getAllCombination(sums, result, count):
    if sums < 0:
        return
        # 数字的组合满足和为sums的条件，打印出所有组合
    if sums == 0:
        print("满足条件的组合：")
        i = 0
        while i < count:
            print(result[i])
            i += 1
        print('\n')
        return
        # 打印debug信息，为了便于理解
    print("----当前组合：")
    i = 0
    while i < count:
        print(str(result[i]))
        i += 1
    print("----")
    # 确定组合中下一个取值
    i = (1 if count == 0 else result[count - 1])
    print("---" + "i=" + str(i) + " count=" + str(count) + "---")  # 打印debug信息，为了便于理解

    while i <= sums:
        result[count] = i
        count += 1
        getAllCombination(sums - i, result, count)  # 求和为sums-i的组合
        count -= 1  # 递归完成后，去掉最后一个组合的数字
        i += 1  # 找下一个数字作为组合中的数字


# 方法功能：找出和为n的所有整数的组合
def showAllCombination(n):
    if n < 1:
        print("参数不满足要求")
        return
    result = [None] * n  # 存储和为n的组合方式
    getAllCombination(n, result, 0)


def main():
    showAllCombination(4)


if __name__ == "__main__":
    main()
