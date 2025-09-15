"""
Problem: String Stack (GeeksforGeeks Practice, Problem ID: 165812)
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/string-stack--165812/1

Given two strings pat and tar consisting of lowercase English characters.
You can construct a new string s by performing any one of the following
operations for each character in pat:
- Append the character pat[i] to the string s.
- Delete the last character of s (if s is empty skip the character).

After performing operations on every character of pat exactly once,
check if it is possible to make the string s equal to string tar.

Approach:
- Use two pointers, i for pat (starting from end) and j for tar (also from end).
- If pat[i] == tar[j], move both pointers back by one.
- If not, simulate the delete operation: skip two characters in pat (i -= 2).
- Continue until either tar is fully matched (j < 0) or pat is exhausted.
- If j < 0 by end, return True, else False.

Time Complexity: O(len(pat) + len(tar))
Space Complexity: O(1) (no extra data structures, constant space aside from input)

"""

class Solution:
    def stringStack(self, pat: str, tar: str) -> bool:
        i = len(pat) - 1
        j = len(tar) - 1
        while i >= 0 and j >= 0:
            if pat[i] == tar[j]:
                i -= 1
                j -= 1
            else:
                i -= 2
        return j < 0
