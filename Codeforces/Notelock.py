for t in range(int(input())):
    n,k=map(int,input().split())
    a=input().strip()
    c=0
    for i in range(n):
        if a[i]=='1':
            ok=False
            for j in range(max(0,i-k+1),i):
                if a[j]=='1':
                    ok=True
                    break
            if not ok:
                c+=1
    print(c)