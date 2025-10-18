'''for t in range(int(input())):
    n,c=map(int,input().split())
    b=list(map(int,input().split()))
    d=list(map(int,input().split()))
    cur=b[:]
    ans=0
    for s in range(n):
        t=c*s
        for i in range(n):
            t*=d[i]*cur[i]
        if t>ans:
            ans=t
        for i in range(n):
            p=i+s+1
            while p<0:
                p+=n
            while p>=n:
                p-=n
            cur[i]=max(cur[i],b[p])
    print(ans)'''
    
    
for t in range(int(input())):
    n,c=map(int,input().split())
    b=list(map(int,input().split()))
    d=list(map(int,input().split()))
    cur=b[:]
    ans=10**18
    for s in range(n):
        t=c*s
        for i in range(n):
            t+=d[i]*cur[i]
        if t<ans:
            ans=t
        for i in range(n):
            p=i-s-1
            while p<0:
                p+=n
            while p>n:
                p-=n
            cur[i]=min(cur[i],b[p])
    print(ans)