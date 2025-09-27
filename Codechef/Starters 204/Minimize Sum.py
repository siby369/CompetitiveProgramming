'''from collections import defaultdict
from sortedcontainers import SortedList

for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    base=sum(a)
    d=defaultdict(SortedList)
    for v in a:
        d[0].add(v)
    sl=d[0]
    r=n
    best=0
    j=0
    for t in range(1,m):
        while j<len(sl) and sl[j]<t:
            r-=1
            j+=1
        x=m-t
        f=n*x-m*r
        if best is None or f<best:
            best=f
    print(base+best)
'''

for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    base=sum(a)
    a.sort()
    r=n
    best=None
    j=0
    for t in range(1,m+1):
        while j<n and a[j]<t:
            r-=1
            j+=1
        x=m-t
        f=n*x-m*r
        if best is None or f<best: 
            best=f
    print(base+best)
