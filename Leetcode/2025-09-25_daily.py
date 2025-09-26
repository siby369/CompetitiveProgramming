"""
Problem: Triangle Minimum Path Sum
Difficulty: Medium
Link: https://leetcode.com/problems/triangle/description/

Approach:
1. We are given a triangle of numbers, and we need to find the minimum path sum from top to bottom.
2. Use dynamic programming (bottom-up modification of the triangle):
   - For each row i starting from the second row:
     • Update the first element: t[i][0] += t[i-1][0]
     • Update the last element: t[i][i] += t[i-1][i-1]
     • For elements in between: t[i][j] += min(t[i-1][j], t[i-1][j-1])
3. After processing all rows, the minimum path sum is the minimum value in the last row.

Time Complexity: O(n^2), n = number of rows (each element processed once).  
Space Complexity: O(1), in-place modification of the triangle.

Notes:
- Can also be solved bottom-up from the last row to the first row.
- In-place DP avoids extra space.
"""

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        n=len(t)
        for i in range(1, n):
            t[i][0]+=t[i-1][0]
            t[i][i]+=t[i-1][i-1]
            for j in range(1, i):
                t[i][j]+=min(t[i-1][j], t[i-1][j-1])
        return min(t[-1])