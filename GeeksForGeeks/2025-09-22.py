"""
Problem: Maximum of Minimum for Every Window Size
Difficulty: Hard
Link: https://www.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1

Approach:
1. The problem asks: for every window size k (1 ≤ k ≤ n), 
   find the maximum of all minimums of every subarray of size k.

2. Key Idea:
   - For each element arr[i], determine the length of the largest window 
     in which arr[i] is the minimum.
   - This can be done using Next Smaller Element (NSE) and Previous Smaller Element (PSE).
   - Window length = NSE[i] - PSE[i] - 1
   - For that window length, arr[i] is a candidate for maximum of minimums.

3. Steps:
   - Use a stack to calculate the nearest smaller element to the left and right.
   - Update ans[length-1] with the maximum value for that window size.
   - Post-process ans so that ans[i] ≥ ans[i+1] (since larger windows inherit values from smaller ones).

Example:
arr = [10, 20, 30, 50, 10, 70, 30]
Result = [70, 30, 20, 10, 10, 10, 10]

Time Complexity: O(n) – each element is pushed/popped at most once.
Space Complexity: O(n) – for stack and auxiliary arrays.

Alternative:
- Can also be solved with two arrays (left, right) for PSE/NSE instead of inline stack updates.
"""

class Solution:
    def maxOfMins(self, arr):
        n=len(arr)
        ans=[0]*n
        st=[]
        for i in range(n):
            while st and arr[i]<arr[st[-1]]:
                idx=st.pop()
                if not st:
                    r=i
                else:
                    r=i-st[-1]-1
                ans[r-1]=max(ans[r-1],arr[idx])
            st.append(i)
        while st:
            idx=st.pop()
            if not st:
                r=n
            else:
                r=n-st[-1]-1
            ans[r-1]=max(ans[r-1],arr[idx])
        for i in range(n-2,-1,-1):
            ans[i]=max(ans[i],ans[i+1])
        return ans
