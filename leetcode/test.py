# -*- coding: utf-8 -*-
from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt_nums = Counter(nums).items()
        return self._generate(cnt_nums, 0)

    def _generate(self, cnt_nums, begin):
        if begin >= len(cnt_nums):
            return [[]]
        cur_num, cur_cnt = cnt_nums[begin]
        result = []
        result.extend(self._generate(cnt_nums, begin + 1))
        for i in xrange(1, cur_cnt+1):
            prefix = [cur_num] * i
            next_gens = self._generate(cnt_nums, begin + 1)
            result.extend([prefix + x for x in next_gens])
        return result


if __name__ == '__main__':
    a = Solution()
    nums = [1,2,2]
    result = a.subsetsWithDup(nums)
    print result