for t in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    if n&1:
        print("No");
        continue
    a=s.count('1')
    r=n-m
    print("Yes" if 0<=n//2-a<=r else "No")