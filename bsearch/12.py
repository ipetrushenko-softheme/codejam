# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        n, m = len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i = i + 1
            j = j + 1

            if i == n:
                return True

        return False
