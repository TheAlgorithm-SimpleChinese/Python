# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 图基础知识.py
@time: 2022/4/21 19:30
"""
"""
图的基础知识:
程序简介：节点与边与权值全部采用整数编号，图采用字典存储
"""

from collections import deque


# 以空格解析输入
def _input(message):
    return input(message).strip().split(" ")


# 初始化（无权）有向图
def initialize_unweighted_directed_graph(node_count: int, edge_count: int) -> dict[int, list[int]]:
    """
       :param node_count:节点数
       :param edge_count: 边数
       :return: 字典
    """
    graph: dict[int, list[int]] = {}  # graph: dict[节点, 与节点相连的其他节点列表] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"边 {e + 1}: 请输入边{e + 1}的两个节点（边与节点都使用整数编号）用空格分隔："))
        graph[x].append(y)
    return graph


# 初始化（无权）无向图
def initialize_unweighted_undirected_graph(node_count: int, edge_count: int) -> dict[int, list[int]]:
    """
    :param node_count:节点数
    :param edge_count: 边数
    :return: 字典
    """

    graph: dict[int, list[int]] = {}  # graph: dict[节点, 与节点相连的其他节点列表] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"边 {e + 1}: 请输入边{e + 1}的两个节点（边与节点都使用整数编号）用空格分隔："))
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
    return graph


# 初始化有权无向图
def initialize_weighted_undirected_graph(node_count: int, edge_count: int) -> dict[int, list[tuple[int, int]]]:
    """
       :param node_count:节点数
       :param edge_count: 边数
       :return: 字典
    """
    graph: dict[int, list[tuple[int, int]]] = {}  # graph: dict[节点, 与节点相连的其他节点与权值的元组] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y, w = (int(i) for i in _input(f"边 {e + 1}: 请输入边{e + 1}的两个节点和权值"
                                          f"（边与节点与权值都使用整数编号）用空格分隔： "))
        graph[x].append((y, w))
        graph[y].append((x, w))
    return graph


if __name__ == "__main__":
    n, m = (int(i) for i in _input("请输入节点数和边数: "))

    graph_choice = int(
        _input(
            "请选择1、2或者3 \n"
            "1. 未加权有向图 \n"
            "2. 未加权无向图 \n"
            "3. 加权无向图 \n请输入你的选择："
        )[0]
    )

    g = {
        1: initialize_unweighted_directed_graph,  # 初始化未加权有向图
        2: initialize_unweighted_undirected_graph,  # 初始化未加权无向图
        3: initialize_weighted_undirected_graph,  # 初始化加权无向图
    }[graph_choice](n, m)


# 深度优先搜索
def dfs(G, s):
    """
    --------------------------------------------------------------------------------
        深度优先搜索：
            Args : G - 边关系字典
                    s - 起始节点
            Vars : vis - 访问节点集（集合）
                    S - 遍历堆栈
    --------------------------------------------------------------------------------
    """
    vis, S = {s}, [s]
    print(s)
    while S:
        flag = 0
        for i in G[S[-1]]:
            if i not in vis:
                S.append(i)
                vis.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            S.pop()


# 广度优先搜索
def bfs(G, s):
    """
    --------------------------------------------------------------------------------
        广度优先搜索。
            Args : G - 边关系字典
                    s - 起始节点
            Vars : vis - 访问节点集
                    Q - 遍历栈
    --------------------------------------------------------------------------------
    """
    vis, Q = {s}, deque([s])
    print(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                vis.add(v)
                Q.append(v)
                print(v)


# 迪杰斯特拉（Dijkstra） 最短路径算法
def dijk(G, s):
    """
    --------------------------------------------------------------------------------
        Dijkstra 最短路径算法
            Args : G - 边关系字典
                    s - 起始节点
            Vars : dist - 存储从 s 到每个其他节点的最短距离的字典
                    known - 一组已知节点
                    path - 路径中的前一个节点
    --------------------------------------------------------------------------------
    """
    global u
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if dist[u] + v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = dist[u] + v[1]
                    path[v[0]] = u
    for i in dist:
        if i != s:
            print(dist[i])


# 拓扑排序
def topo(G, ind=None, Q=None):
    """
    --------------------------------------------------------------------------------
        拓扑排序
    --------------------------------------------------------------------------------
    """
    if Q is None:
        Q = [1]
    if ind is None:
        ind = [0] * (len(G) + 1)  # 索引被忽略
        for u in G:
            for v in G[u]:
                ind[v] += 1
        Q = deque()
        for i in G:
            if ind[i] == 0:
                Q.append(i)
    if len(Q) == 0:
        return
    v = Q.popleft()
    print(v)
    for w in G[v]:
        ind[w] -= 1
        if ind[w] == 0:
            Q.append(w)
    topo(G, ind, Q)


def adjm():
    """
    --------------------------------------------------------------------------------
        读取邻接矩阵
    --------------------------------------------------------------------------------
    """
    n = input().strip()
    a = []
    for i in range(n):
        a.append(map(int, input().strip().split()))
    return a, n


def floy(A_and_n):
    """
    --------------------------------------------------------------------------------
        Floyd Warshall 算法
            Args : G - 边关系字典
                    s - 起始节点
            Vars : dist - 存储从 s 到每个其他节点的最短距离的字典
                    known - 一组已知节点
                    path - 路径中的前一个节点

    --------------------------------------------------------------------------------
    """
    (A, n) = A_and_n
    dist = list(A)
    path = [[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][k] = k
    print(dist)


def prim(G, s):
    """
    --------------------------------------------------------------------------------
        Prim 的 MST 算法
            Args : G - 边关系字典
                    s - 起始节点
            Vars : dist - 存储从 s 到最近节点的最短距离的字典
                    known - 一组已知节点
                    path - 路径中的前一个节点
    --------------------------------------------------------------------------------
    """
    global u
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = v[1]
                    path[v[0]] = u
    return dist


def edglist():
    """
    --------------------------------------------------------------------------------
        接受边列表
            Vars : n - 节点数
                   m - 边数
            返回： l - 边列表
                  n - 节点数
    --------------------------------------------------------------------------------
    """
    n, m = map(int, input().split(" "))
    edges = []
    for i in range(m):
        edges.append(map(int, input().split(" ")))
    return edges, n


def krusk(E_and_n):
    """
    --------------------------------------------------------------------------------
        Kruskal 的 MST 算法
            Args : E - 边列表
                    n - 节点数
            Vars : s - 所有节点的集合作为唯一的不相交集（最初）
    --------------------------------------------------------------------------------
    """
    # 根据距离对边进行排序
    global i
    (E, n) = E_and_n
    E.sort(reverse=True, key=lambda x: x[2])
    s = [{i} for i in range(1, n + 1)]
    while True:
        if len(s) == 1:
            break
        print(s)
        x = E.pop()
        for i in range(len(s)):
            if x[0] in s[i]:
                break
        for j in range(len(s)):
            if x[1] in s[j]:
                if i == j:
                    break
                s[j].update(s[i])
                s.pop(i)
                break


# 找出图的的孤立节点
def find_isolated_nodes(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated
