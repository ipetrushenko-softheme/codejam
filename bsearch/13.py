# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bad = -1
        good = n + 1
        while good - bad > 1:
            m = (good + bad) // 2
            if guess(m) >= 0:
                bad = m
            else:
                good = m
        return bad
