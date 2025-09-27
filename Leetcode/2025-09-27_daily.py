"""
Problem: Largest Triangle Area
Difficulty: Easy
Link: https://leetcode.com/problems/largest-triangle-area/description/

Approach:
- We are given a set of 2D points and need to find the maximum area of any triangle formed by three points.
- Use the **Shoelace Formula** (determinant method) to compute the area of a triangle formed by three points:
    Area = 0.5 * | x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) |
- Iterate over all possible triplets of points:
    • For each (i, j, k), calculate the area.
    • Keep track of the maximum area found.

Time Complexity: O(n^3), since we check all triplets.  
Space Complexity: O(1), only storing intermediate results.
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    current_area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
                    max_area = max(max_area, current_area)
                    
        return max_area