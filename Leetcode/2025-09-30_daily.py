"""
Problem: Find Triangular Sum of an Array
Difficulty: Easy
Link: https://leetcode.com/problems/find-triangular-sum-of-an-array/

Approach:
- We repeatedly reduce the array until only one number remains.
- At each step:
  1. Replace the array with a new array where each element is:
     (nums[i] + nums[i+1]) % 10
  2. Continue this process until the array length becomes 1.
- The final single number is the triangular sum.

Time Complexity: O(n^2)
- Each reduction step processes one fewer element than before, giving n + (n-1) + ... + 1 ≈ O(n^2).
Space Complexity: O(n)
- A temporary list is created in each step.
"""

class Solution:
    def triangularSum(self, nums):
        l1 = []

        while len(nums) != 1:
            for i in range(len(nums)-1):
                number = (nums[i] + nums[i+1]) % 10
                l1.append(number)
            nums = l1[:]
            l1 = []
        return nums[0]