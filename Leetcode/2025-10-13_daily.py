class Solution(object):
    def removeAnagrams(self, words):
        ans = [words[0]]
        for i in range(1, len(words)):
            a, b = sorted(words[i]), sorted(ans[-1])
            if a != b:
                ans.append(words[i])
        return ans