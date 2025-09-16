"""
Problem: 4A. Watermelon
Difficulty: Easy
Link: https://codeforces.com/problemset/problem/4/A

Approach:
- The weight w must be split into two positive even integers.
- For this to be possible:
  - w must be even
  - w > 2 (since 2 cannot be split into two positive even numbers)
- If both conditions are satisfied, print "YES"; otherwise, "NO".

Time Complexity: O(1)
Space Complexity: O(1)
"""

n=int(input())
if n&1==0 and n>2:
    print("YES")
else:
    print("NO")