"""
Contest: CodeChef Starters 203
Problem: Passing Grade
Link: https://www.codechef.com/problems/PASSINGGR
Difficulty: Easy

Approach:
- First element `c` is the cutoff grade.
- Count how many elements in the array are greater than or equal to `c`.
- Print the count for each test case.

Time Complexity: O(n) per test case.
Space Complexity: O(1), apart from input storage.
"""

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=a[0]
    k=sum(1 for x in a if x>=c)
    print(k)
