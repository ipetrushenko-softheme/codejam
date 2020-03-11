# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        ans = []
        for r in range(rows):
            idx = self.bs(mat[r])
            ans.append((idx, r))

        ordered = sorted(ans, key=lambda tup: tup[0])
        first = ordered[:k]
        return [el[1] for el in first]

    def bs(self, arr: List[int]) -> int:
        bad = len(arr)
        good = -1

        while bad - good > 1:
            m = (good + bad) // 2
            if arr[m] == 0:
                bad = m
            else:
                good = m

        return good
