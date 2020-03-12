# https://leetcode.com/problems/valid-perfect-square/submissions/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        bad = -1
        good = num + 1
        while good - bad > 1:
            m = (good + bad) // 2
            if m * m >= num:
                good = m
            else:
                bad = m

        return good * good == num