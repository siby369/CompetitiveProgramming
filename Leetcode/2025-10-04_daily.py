"""
Problem: Container With Most Water
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

Approach:
- The problem asks for two lines that together with the x-axis form a container that holds the most water.
- The area between two lines is determined by:
    area = (right_index - left_index) * min(height[left], height[right])
- To maximize this area efficiently:
  1. Use a two-pointer approach — one at the start (`l`) and one at the end (`r`).
  2. Calculate the area and update the maximum.
  3. Move the pointer corresponding to the smaller height inward:
     - Because the height of the smaller line limits the area, moving it may lead to a taller line and possibly a larger area.
  4. Repeat until the two pointers meet.

Time Complexity: O(n)
- Each element is visited at most once.
Space Complexity: O(1)
- Constant extra space used.

Key Insight:
- The brute force approach (O(n²)) checks all pairs, but with two pointers,
  we efficiently eliminate impossible cases based on height constraints.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=m=0
        r=n-1
        while l<r :
            m=max(m,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m