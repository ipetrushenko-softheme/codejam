# https://leetcode.com/problems/arranging-coins/submissions/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 0
        for i in range(1, n+1):
            s += i
            if s > n:
                return i - 1
        return n
