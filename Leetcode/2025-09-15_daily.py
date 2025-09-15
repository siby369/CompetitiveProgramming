"""
Problem: 1935. Maximum Number of Words You Can Type
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

Approach:
- Split the text into words.
- For each word, check if it contains any broken letter.
- If no broken letter is present, count it as typeable.

Time Complexity: O(n * m), where n = number of words, m = average word length.
Space Complexity: O(1), only counters and flags used.
"""  

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        w=text.split()
        count=0
        for i in w:
            flag=False
            for j in i:
                if j in brokenLetters:
                    flag=True
                    break
            if not flag:
                count+=1
        return count
        
        '''w=text.split()
        count=len(w)
        temp=set()
        for j in range(len(brokenLetters)):
            for i in range(len(w)):
                if brokenLetters[j] in w[i]:
                    if w[i] not in temp:
                        count-=1
                        temp.add(w[i])
        return count'''

