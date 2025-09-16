"""
Problem: 71A. Way Too Long Words
Difficulty: Easy
Link: https://codeforces.com/problemset/problem/71/A

Approach:
- Read the number of test cases t.
- For each word:
  - If the length is <= 10, print the word directly.
  - Otherwise, print first letter + (length - 2) + last letter.
- This ensures words longer than 10 characters are abbreviated.

Time Complexity: O(n), where n = total number of characters across all words.
Space Complexity: O(1), only counters and string operations used.
"""

for t in range(int(input())):
    w=input()
    n=len(w)
    if n<=10:
        print(w)
    else:
        print(f"{w[0]}{len(w)-2}{w[-1]}")