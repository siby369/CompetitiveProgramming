for t in range(int(input())):
    x,y=map(int,input().split())
    g=(x+y)/3
    s=0
    for i in range(int(g)):
        if y>0:
            s+=2
            y-=1
        else:
            s+=1
    print(s)