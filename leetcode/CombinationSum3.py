# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self._choose(1, 9, k, n)

    def _choose(self, begin, end, k, n):
        result = []
        if k == 1:
            if begin <= n <= end:
                return [[n]]
            else:
                return result
        for i in xrange(begin, end - k + 2):
            others = self._choose(i + 1, end, k - 1, n - i)
            for ot in others:
                ot.insert(0, i)
                result.append(ot)
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.combinationSum3(4, 24)
    print result