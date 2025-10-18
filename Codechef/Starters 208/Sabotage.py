'''for t in range(int(input())):
    n,x,k=map(int,input().split())
    a=sorted(map(int,input().split()))
    c=0
    for s in a[k:]:
        if s>x+100*k:
            c+=1
    print(c+1)'''

'''for t in range(int(input())):    
    n,x,k=map(int,input().split())
    a=sorted(map(int,input().split()))
    for i in range(k):
        a[i]=0
        x+=100
    c=0
    for s in a:
        if s>x:
            c+=1
    print(c+1)'''
    
for t in range(int(input())):    
    n,x,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    i=0
    while i<n and k>0:
        if a[i]>x:
            a[i]=0
            x+=100
            k-=1
        i+=1
    h=0
    for v in a:
        if v>x:
            h+=1
    print(h+1)