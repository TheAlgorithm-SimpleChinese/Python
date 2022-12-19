# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 只出现一次的数字.py
@time: 2022/12/19 21:20
"""
from functools import reduce
from typing import List

"""
解题思路：
拿到这道题，若不考虑复杂度，相信大家都能做出来，但是最终的复杂度基本都是n^2。
这道题的真实目的其实是在考察我们能否用线性的时间和常量的空间来完成。
如何实现呢？答案呼之欲出，我们应该使用位运算其中的异或运算。
首先针对异或运算，这里做一个知识点的总结：
任何数和自己做异或运算，结果为 00，即 a⊕a=0a⊕a=0 。
任何数和 00 做异或运算，结果还是自己，即 a⊕0=⊕a⊕0=⊕。
异或运算中，满足交换律和结合律，也就是 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=ba⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    solve1 = Solution()
    print(solve1.singleNumber([2, 2, 1]))
