"""
Problem: Largest Perimeter Triangle
Difficulty: Easy
Link: https://leetcode.com/problems/largest-perimeter-triangle/

Approach:
- A triangle is valid if the sum of any two sides is greater than the third.
- To maximize perimeter:
  1. Sort the array in descending order.
  2. Check the largest three sides:
     - If nums[0] < nums[1] + nums[2], they form a valid triangle.
     - Else, remove nums[0] (too large to form a valid triangle) and repeat.
- Continue until a valid triplet is found or fewer than 3 numbers remain.

Time Complexity: O(n log n), due to sorting.
Space Complexity: O(1), aside from sorting in place.
"""
