for t in range(int(input())):
    n,a,b=map(int,input().split())
    m=999999
    for i in range(n):
        x,y=map(int,input().split())
        d=abs(a-x)+abs(b-y)
        if d<m:
            m=d
    print(m)