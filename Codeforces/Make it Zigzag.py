for t in range(int(input())):
    t-=1
    n=int(input())
    a=[0]+list(map(int,input().split()))
    x=[0]*(n+1)
    x[1]=a[1]
    for i in range(2,n+1):
        x[i]=max(x[i-1],a[i])
    for i in range(n-1,0,-1):
        if i&1:
            x[i]=min(x[i],x[i+1]-1)
        elif x[i]<=x[i+1]:
            x[i+1]=x[i]-1
    ans=0
    for i in range(1,n+1):
        if a[i]>x[i]:
            ans+=a[i]-x[i]
    print(ans)