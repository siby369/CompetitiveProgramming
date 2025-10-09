class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        zeroes = []
        ans = [-1] * len(rains)
        dic = {}

        for i in range(len(rains)):
            if rains[i] == 0:
                ans[i]=1
                zeroes.append(i)
            else:
                if rains[i] not in dic:
                    dic[rains[i]] = i
                else:
                    pos = bisect.bisect_left(zeroes, dic[rains[i]])
                    if pos < len(zeroes):
                        ans[zeroes[pos]] = rains[i]
                        zeroes.pop(pos)
                    else:return []
                    dic[rains[i]] = i 

        return ans