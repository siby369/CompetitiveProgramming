"""
Problem: Decode the String
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/decode-the-string2444/1

Approach:
- We need to decode an encoded string with patterns like "3[a2[c]]" → "accaccacc".
- Use a stack-based approach but traverse the string **from right to left**:
  - If the current character is not '[', push it to the stack.
  - If it is '[', it indicates the start of a substring to be expanded:
    - Pop characters until ']' to build the substring (`cur`).
    - Pop any extra part that follows (`mkp`).
    - Move left to collect the full number (`p`) representing the repetition count.
    - Repeat the substring `t` times and push it back to the stack, appending `mkp`.
- At the end, the top of the stack contains the fully decoded string.

Time Complexity: O(n * k), where n = length of input string and k = maximum repeat count (since substring concatenation happens k times).
Space Complexity: O(n), for the stack used to hold characters and substrings during decoding.
"""



class Solution:
    def decodedString(self,s):
        st=[]
        i=len(s)-1
        while i>=0:
            if s[i]=='[':
                cur=""
                while st and st[-1]!="]":
                    cur+=st.pop()
                st.pop()
                mkp=""
                while st and st[-1]!="]":
                    mkp+=st.pop()
                i-=1
                p=""
                while i>=0 and s[i].isdigit():
                    p+=s[i]
                    i-=1
                p=p[::-1]
                t=int(p)
                newTemp=""
                for k in range(t):
                    newTemp+=cur
                st.append(newTemp+mkp)
            else:
                p=s[i]
                st.append(p)
                i-=1
        return st[-1]
