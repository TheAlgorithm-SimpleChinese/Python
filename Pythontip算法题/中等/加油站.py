# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 加油站.py
@time: 2022/8/22 14:20
"""
n = 2
limit = [1, 2]
cost = [2, 2]
gas_station = []  # 能完成任务的加油站编号列表
for i in range(n):  # 从第0个加油站作为起点开始算
    gas_total = 0  # 汽车的油量
    station_num = 0  # 经过加油站的个数
    for j in range(i, n + i):  # 从第i个加油站开始，走一圈回到i
        if j >= n:
            j = j - n  # 如果加油站索引超出范围，则减去n
        gas_total += limit[j]  # 加油
        if gas_total >= cost[j]:
            station_num += 1  # 如果能通过，经过加油站的数量+1
            gas_total -= cost[j]  # 减去消耗的油量
        else:
            break  # 如果不能通过，跳出本层循环
    if station_num == n:
        gas_station.append(i)  # 如果经过加油站数量为n，则说明能完成，把起点i加入
# 最后输出结果：
if gas_station:
    print(min(gas_station))  # 打印最小编号
else:
    print(-1)
