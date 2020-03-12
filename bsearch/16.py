# https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        good = 0
        bad = n + 1
        while bad - good > 1:
            m = (good + bad) // 2
            if isBadVersion(m):
                bad = m
            else:
                good = m
        return bad
