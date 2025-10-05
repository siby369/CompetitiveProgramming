'''for t in range(int(input())):
    n=int(input())
    mx=(n-2)*(n-1)//2
    s=[0]*n
    mn=0
    for i in range(n-1):
        s.sort()
        a=s[0]
        b=s[1]
        mn+=a+b
        s[0]=a+1
    print(mn,mx)
'''
'''
import heapq
for t in range(int(input())):
    n=int(input())
    h=[0]*n
    heapq.heapify(h)
    mn=0
    for i in range(n-1):
        a=heapq.heappop(h)
        b=heapq.heappop(h)
        mn+=a+b
        heapq.heappush(h,a+1)
    arr=[0]*n
    mx=0
    for i in range(n-1):
        arr.sort(reverse=True)
        a=arr[0]
        b=arr[1]
        mx+=a+b
        arr[0]=a+1
    print(mn,mx)
'''


for t in range(int(input())):
    n=int(input())
    if n==2:
        minsum=0 
    else:
        minsum=n-2
    maxsum=(n-1)*(n-2)//2
    print(minsum,maxsum)