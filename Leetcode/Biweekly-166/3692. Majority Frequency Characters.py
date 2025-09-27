from collections import Counter
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        f=Counter(s)
        g=defaultdict(list)
        for c,n in f.items():
            g[n].append(c)
        ans=[]
        freq=0
        for k,v in g.items():
            if len(v)>len(ans) or(len(v)==len(ans) and k>freq):
                ans=v
                freq=k
        return ''.join(ans)
