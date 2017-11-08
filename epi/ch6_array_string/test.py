# -*- coding: utf-8 -*-

import random
from epi.ch6_array_string import sort

if __name__ == '__main__':
    nums = [random.randint(1, 1000) for i in range(10)]
    print nums
    sort.quick_sort_dutch_flag(nums)
    print nums