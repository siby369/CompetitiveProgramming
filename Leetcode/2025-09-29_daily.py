"""
Problem: Minimum Score Triangulation of Polygon
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Approach:
- We are given a convex polygon with vertex values.
- Each triangle (i, j, k) contributes a score = values[i] * values[j] * values[k].
- Goal: triangulate polygon into n-2 triangles with minimum total score.

Dynamic Programming (Recursion + Memoization):
1. Define state:
   - dp[i][j] = minimum score to triangulate the polygon section from vertex i to j.
2. Base Case:
   - If (j - i < 2), fewer than 3 vertices → no triangle → score = 0.
3. Transition:
   - For each possible k between (i, j):
     dp[i][j] = min(dp[i][j],
                    dp[i][k] + values[i]*values[k]*values[j] + dp[k][j])
   - This ensures we pick the triangulation that minimizes the total score.
4. Memoization:
   - Use a 2D dp array to store computed results and avoid recomputation.

Time Complexity: O(n^3)
- There are O(n^2) states, and for each state we try up to O(n) splits.
Space Complexity: O(n^2)
- For the DP memoization table.
"""

class Solution:
    def __init__(self):
        self.dp = [[0] * 50 for _ in range(50)]
        
    def minScoreTriangulation(self, values, i=0, j=0, res=0):
        if j == 0:
            j = len(values) - 1
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        for k in range(i + 1, j):
            res = min(res if res != 0 else float('inf'),
                self.minScoreTriangulation(values, i, k) +
                values[i] * values[k] * values[j] +
                self.minScoreTriangulation(values, k, j))
        self.dp[i][j] = res
        return self.dp[i][j]