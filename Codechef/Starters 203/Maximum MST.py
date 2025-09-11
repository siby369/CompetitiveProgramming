"""
Contest: CodeChef
Problem: Maximum MST (MAXMST7)
Link: https://www.codechef.com/problems/MAXMST7
Difficulty: Medium

Approach:
- The graph has n nodes and m = n*(n-1)//2 edges (complete graph).
- Read all edge weights and sort them in non-decreasing order.
- In the maximum spanning tree:
  - The k-th vertex contributes its minimum edge to the MST.
  - That edge is located at index k*(k-1)//2 in the sorted edge list.
- Accumulate these edges to get the maximum MST weight.

Time Complexity: O(m log m), due to sorting (m = n*(n-1)//2).
Space Complexity: O(m), for storing edge weights.
"""

for t in range(int(input())):
    n=int(input())
    m=n*(n-1)//2
    a=[]
    while len(a)<m:
        a+=list(map(int,input().split()))
    a.sort()
    s=0
    k=1
    while k<n:
        s+=a[k*(k-1)//2]
        k+=1
    print(s)
