"""
Problem: 2197. Replace Non-Coprime Numbers in Array
Difficulty: Hard
Link: https://leetcode.com/problems/replace-non-coprime-numbers-in-array

Approach:
- Use a stack to maintain the processed numbers.
- For each number in the input array:
  - Push it to the stack.
  - While the top two elements of the stack are not coprime (gcd > 1):
    - Pop both numbers and replace them with their LCM.
- This ensures adjacent non-coprimes are repeatedly merged until only coprimes remain.

Time Complexity: O(n * log(max(nums))), since gcd calculations are logarithmic in the size of numbers.
Space Complexity: O(n), for the stack to hold the processed numbers.
"""

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s=[]
        for i in nums:
            s.append(i)
            while len(s)>1:
                g=gcd(s[-1],s[-2])
                if g>1:
                    a=s.pop()
                    b=s.pop()
                    s.append(a*b//g)
                else:
                    break
        return s
