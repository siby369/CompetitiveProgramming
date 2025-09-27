'''from collections import deque
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=False
    for s in range(n):
        v=set()
        q=deque([s])
        while q:
            p=q.popleft()
            for x in range(n):
                if x!=p and (p-x)%a[p]==0:
                    q.append(x)
        if len(v)==0:
            f=True
    print("Yes" if f else "No")

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if 2 in a:
        print("Yes")
    else:
        print("No")'''
        
for t in range(int(input())):      
    n=int(input())
    a=list(map(int,input().split()))
    o=False
    e=False
    for i in range(n):
        if a[i]==1:
            if (i+1)%2:
                o=True
            else:
                e=True
    if o and e:
        print("No")
    else:
        print("Yes")