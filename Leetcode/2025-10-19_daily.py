class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        arr = set()
        arr.add(s)
        li = []
        li.append(s)
        while li :
            s = li.pop(0)
            l = list(s)
            for j in range(len(s)) :
                arr.add(s)
                li.append(s)
        return min(arr)     