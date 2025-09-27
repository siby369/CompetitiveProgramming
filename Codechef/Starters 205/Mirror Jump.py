for t in range(int(input())):
    n,k=map(int,input().split())
    d={k:0}
    s=[k]
    while s:
        p=s.pop(0)
        if p==n:
            print(d[p])
            break
        for x in [p-1,p+1,n+1-p]:
            if 1<=x<=n and x not in d:
                d[x]=d[p]+1
                s.append(x)