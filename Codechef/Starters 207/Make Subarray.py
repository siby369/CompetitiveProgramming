for t in range(int(input())):
    n=int(input())
    s=input()
    if '1' not in s:
        print(0)
    else:
        f=s.index('1')
        l=s[::-1].index('1')
        print(s[f:n-l].count('0'))