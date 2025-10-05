# cook your dish here
def isprime(n):
    if n==1 or n==0:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    l=5
    while l*l<=n:
        if n%l==0 or n%(l+2)==0:
            return False
        l+=6
    return True
    
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if isprime(a[i]+a[j]):
                count+=1
    print(count)