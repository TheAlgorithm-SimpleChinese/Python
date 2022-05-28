# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 散列表基础.py
@time: 2022/4/22 22:39
"""


def check_prime(number):
    """
    判断一个数是否是素数（这不是最好的办法）
    如是实参是0或者1,则返回2,实参是2则返回3
    """
    special_non_primes = [0, 1, 2]
    if number in special_non_primes[:2]:
        return 2
    elif number == special_non_primes[-1]:
        return 3

    return all(number % i for i in range(2, number))


def next_prime(value, factor=1, **kwargs):
    """
    :param value: 值
    :param factor: 影响因子
    :param kwargs: 其他
    :return: 找出大于factor * value的最小素数
    """
    value = factor * value
    first_value_val = value

    while not check_prime(value):  # 当value不是一个素数时
        value += 1 if not ("desc" in kwargs.keys() and kwargs["desc"] is True) else -1

    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value


class HashTable:
    """
    具有开放寻址和线性探测的基本哈希表
    """

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
        self._keys = {}

    def keys(self):
        return self._keys

    def balanced_factor(self):
        """
        平衡因子
        :return:
        """
        return sum(1 for slot in self.values if slot is not None) / (
                self.size_table * self.charge_factor
        )

    def hash_function(self, key):
        """
        散列函数
        """
        return key % self.size_table

    def _step_by_step(self, step_ord):

        print(f"step {step_ord}")
        print([i for i in range(len(self.values))])
        print(self.values)

    def bulk_insert(self, values):
        """
        块插入
        """
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
        self.values[key] = data
        self._keys[key] = data

    def _collision_resolution(self, key, data=None):
        """
        冲突解决
        """
        new_key = self.hash_function(key + 1)

        while self.values[new_key] is not None and self.values[new_key] != key:

            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return new_key

    def rehashing(self):
        """
        再散列
        """
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table
        for value in survivor_values:
            self.insert_data(value)

    def insert_data(self, data):
        """
        插入数据
        """
        key = self.hash_function(data)

        if self.values[key] is None:
            self._set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            collision_resolution = self._collision_resolution(key, data)
            if collision_resolution is not None:
                self._set_value(collision_resolution, data)
            else:
                self.rehashing()
                self.insert_data(data)


def main():
    hash1 = HashTable(18)
    hash1.bulk_insert([x for x in range(30)])
    print(hash1.keys())


if __name__ == '__main__':
    main()
