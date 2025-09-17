"""
Problem: (https://codeforces.com/contest/2143/problem/A)

Statement (inferred from code):
- Given t test cases.
- For each test case, you are given:
  - An integer n.
  - A list p of length n.
- You must determine if it is possible to assign numbers 1..n (each used at most once) 
  according to certain constraints defined by p and the construction logic.
- Print "YES" if possible, otherwise "NO".

Approach:
- Maintain:
  - `used`: boolean array to track whether a number (1..n) has been used.
  - `ends`: array where `ends[i]` tracks contributions that should end at position i.
  - `prev`: stores the previous prefix value.
- Iterate over each position i:
  - Compute `s = p[i] - prev + cur` where `cur = ends[i-1]` (or 0 if i=0).
    - If s < 0, it's invalid → break.
  - If s > 0, select `s` unused numbers from n..1 greedily (largest available first).
    - If unable to pick exactly `s`, mark invalid.
  - Mark chosen numbers as used and update `ends` accordingly.
  - Update prev = p[i].
- After processing all i:
  - If never failed → print "YES"
  - Otherwise → print "NO".

Time Complexity:
- O(n^2) in the worst case per test (nested loop picking elements).
- Optimizations may exist, but this brute greedy approach ensures correctness within constraints.

Space Complexity:
- O(n) for arrays `used` and `ends`.
"""

for t in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    used=[False]*(n+1)
    ends=[0]*n
    prev=0
    ok=True
    for i in range(n):
        cur=ends[i-1] if i>0 else 0
        s=p[i]-prev+cur
        if s<0:
            ok=False
            break
        use=[]
        if s>0:
            cnt=s
            for k in range(n,0,-1):
                if not used[k] and i+k<=n:
                    use.append(k)
                    cnt-=1
                    if cnt==0:break
        if len(use)!=s:
            ok=False
            break
        for k in use:
            used[k]=True
            if i+k-1<n:
                ends[i+k-1]+=1
        prev=p[i]
    print("YES" if ok else "NO")
