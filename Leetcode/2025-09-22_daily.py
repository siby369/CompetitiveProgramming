"""
Problem: Count Elements With Maximum Frequency
Difficulty: Easy
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/

Approach:
1. Create a frequency array `freq` of size 101 (since 1 <= nums[i] <= 100).
2. Traverse `nums`:
   - Count frequency of each element.
   - Track the maximum frequency `maxF`.
3. Traverse `freq` again:
   - For each frequency equal to `maxF`, add it to the answer.
   - This effectively counts how many elements appear with the maximum frequency.
4. Return the total.

Example:
nums = [1,2,2,3,1,4]
- freq[1] = 2, freq[2] = 2, others <= 1
- maxF = 2
- Elements with max frequency = {1, 2}
- Answer = 2 + 2 = 4

Time Complexity: O(n + k), where n = len(nums), k = 100 (constant).
Space Complexity: O(1), since `freq` size is fixed (101).
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=[0]*101
        maxF=0
        for x in nums:
            freq[x]+=1
            maxF=max(maxF, freq[x])
        ans=0
        for f in freq:
            if f==maxF:
                ans+=f
        return ans