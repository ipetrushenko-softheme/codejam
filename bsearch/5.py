# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        r = len(grid) - 1
        cols = len(grid[0])
        count = 0
        while r > -1 and c < cols:
            if grid[r][c] < 0:
                count += cols - c
                r = r - 1
            else:
                c = c + 1
        return count


s = Solution()
print(s.countNegatives([
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]))

# def countNegatives(self, grid: List[List[int]]) -> int:
#     rows = len(grid)
#     sum = 0
#     for i in range(rows):
#         sum += self.binsearch(grid[i])
#     return sum

# def binsearch(self, a: List[int]) -> int:
#     bad = -1
#     good = len(a)
#     while good - bad > 1:
#         m = (good + bad) // 2
#         if a[m] < 0:
#             good = m
#         else:
#             bad = m
#     return len(a) - good
