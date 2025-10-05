# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    print(sum(sorted(s,reverse=True)[:k]))