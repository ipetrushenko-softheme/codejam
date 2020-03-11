
# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/submissions/

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, z + 1):
            y = self.bs(x, z, customfunction)
            if y != -1:
                ans.append([x, y])
        return ans

    def bs(self, x, z, customfunction):
        bad = 0
        good = z + 1
        while good - bad > 1:
            m = (good + bad) // 2
            if customfunction.f(x, m) >= z:
                good = m
            else:
                bad = m

        if customfunction.f(x, good) == z:
            return good
        return -1