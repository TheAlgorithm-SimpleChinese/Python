# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 找出数组中元素的的最大值和最小值_变形的分治法.py
@time: 2022/4/18 15:48
"""

"""
** 方法功能：找出数组中的最大值和最小值
"""


# 返回值列表中有两个元素，第一个元素为子数组的最小值，第二个元素为最大值
def getMaxMin(array, left, right):
    if array is None:
        print("参数不合法")
        return
    list = []
    m = int((left + right) / 2)  # 求中点,如果是奇数则转为整数
    if left == right:  # 如果列表只有一个元素
        list.append(array[left])
        list.append(array[left])
        return list
    if left + 1 == right:  # 如果列表只有两个元素
        if array[left] >= array[right]:
            max = array[left]
            min = array[right]
        else:
            max = array[right]
            min = array[left]
        list.append(min)
        list.append(max)
        return list
    # 递归计算左半部分
    leftList = getMaxMin(array, left, m)
    # 递归计算右半部分
    rightList = getMaxMin(array, m + 1, right)
    # 总的最大值
    max = leftList[1] if (leftList[1] > rightList[1]) else rightList[1]
    # 总的最小值
    min = leftList[0] if (leftList[0] < rightList[0]) else rightList[0]
    list.append(min)
    list.append(max)
    return list


def main():
    array = [7, 3, 19, 40, 4, 7, 1]
    result = getMaxMin(array, 0, len(array) - 1)
    print("最大值为：" + str(result[1]))
    print("最小值为：" + str(result[0]))


if __name__ == "__main__":
    main()
