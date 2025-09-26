"""
Problem: Valid Triangle Number
Difficulty: Medium
Link: https://leetcode.com/problems/valid-triangle-number/

Approach:
1. Sort the input array `nums`.
2. Use a three-pointer strategy to count all triplets (i, j, k) that satisfy the triangle inequality:
   - For a valid triangle: nums[i] + nums[j] > nums[k]
3. Iterate from the largest element to the smallest (as `nums[k]`):
   - Initialize two pointers: `left = 0` and `right = k - 1`.
   - While left < right:
     - If nums[left] + nums[right] > nums[k], all pairs between left and right are valid:
       • Increment count by `right - left`.
       • Move `right` pointer leftward.
     - Else, move `left` pointer rightward.
4. Return the total count of valid triangles.

Time Complexity: O(n^2), due to the two-pointer nested loop after sorting.
Space Complexity: O(1), aside from the sorting space.
"""


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count