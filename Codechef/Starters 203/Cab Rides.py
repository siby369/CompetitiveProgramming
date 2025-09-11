"""
Contest: CodeChef Starters 203
Problem: Exams (or equivalent problem for this code)
Link: https://www.codechef.com/problems/CABRIDE
Difficulty: Easy

Approach:
- Given n, divide it by 4 → quotient q and remainder r.
- Based on remainder:
  - r == 0 → cost = q*400
  - r == 1 → if q>0, cost = (q-1)*400+500, else cost = 200
  - r == 2 → cost = q*400+200
  - r == 3 → cost = q*400+300
- Print the cost.

Time Complexity: O(1) per test case.
Space Complexity: O(1).
"""

for t in range(int(input())):
    n=int(input())
    q,r=divmod(n,4)
    c=0
    if r==0:
        c=q*400
    elif r==1:
        if q:
            c=(q-1)*400+500
        else:
            c=200
    elif r==2:
        c=q*400+200
    else:
        c=q*400+300
    print(c)
