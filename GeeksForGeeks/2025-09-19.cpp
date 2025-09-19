/*
Problem: Minimum Add to Make Parentheses Valid
Difficulty: Easy
Link: https://www.geeksforgeeks.org/problems/minimum-number-of-parentheses/1

Approach:
- We need to find the minimum number of parentheses insertions required 
  to make a string of '(' and ')' valid.
- Use two counters:
  - `st`: tracks unmatched '(' (open brackets).
  - `res`: tracks unmatched ')' (close brackets).
- Traverse the string:
  - If the character is '(', increment `st`.
  - If the character is ')':
    - If `st > 0`, match it with a previous '(', so decrement `st`.
    - Otherwise, increment `res` (unmatched ')').
- At the end:
  - `st` holds unmatched '(' that need closing.
  - `res` holds unmatched ')' that need opening.
- The answer is `res + st`.

Time Complexity: O(n), single pass over the string.  
Space Complexity: O(1), constant extra space.
*/

class Solution 
{
  public:
    int minParentheses(string& s) 
    {
        int res = 0, st = 0;
        for(auto it : s)
        {
            if(it=='(')
            st++;
            else if(st)
            st--;
            else
            res++;
        }
        return res+st;
    }
};