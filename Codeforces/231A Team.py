"""
Problem: 231A. Team
Difficulty: Easy
Link: https://codeforces.com/problemset/problem/231/A

Approach:
- For each problem, read the opinions of the three friends (as a string of three numbers).
- Count how many of them are sure about the solution (i.e., how many '1's).
- If at least two are sure, the team will implement the problem.
- Count and print the total number of problems the team will implement.

Time Complexity: O(n), where n is the number of problems.
Space Complexity: O(1), only a counter is used.
"""

c=0
for t in range(int(input())):
    s=input().count('1')
    if s>=2:
        c+=1 
print(c)