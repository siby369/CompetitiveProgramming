/*
Problem: Longest Subarray with Elements Less Than or Equal to Length
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/longest-subarray-length--202010/1

Approach:
- Given an array, we want the length of the longest contiguous subarray 
  such that each element is ≤ length of the subarray.
- Use **monotonic stacks** to find the next greater and previous greater elements:
  - `next[i]`: index of the next element greater than `arr[i]` (or n if none).
  - `prev[i]`: index of the previous element greater than `arr[i]` (or -1 if none).
- Steps:
  1. Traverse from left to right to fill `next[]`.
  2. Traverse from right to left to fill `prev[]`.
  3. For each element `arr[i]`, calculate subarray length `l = next[i] - prev[i] - 1`.
  4. If `arr[i] <= l`, update the answer `ans = max(ans, l)`.
- This efficiently checks all subarrays where `arr[i]` is the maximum element.

Time Complexity: O(n), each element is pushed and popped at most once from the stack.  
Space Complexity: O(n), for `next[]`, `prev[]`, and the stack.
*/


class Solution
{
public:
    int longestSubarray(vector<int>&arr)
    {
        int n=arr.size();
        stack<int>ss;
        vector<int>next(n,n),prev(n,-1);
        for(int i=0;i<n;i++){
            while(ss.size() && arr[ss.top()]<arr[i])
            {
                next[ss.top()]=i;
                ss.pop();
            }
            ss.push(i);
        }
        while(ss.size())ss.pop();
        for(int i=n-1;i>=0;i--)
        {
            while(ss.size() && arr[ss.top()]<arr[i])
            {
                prev[ss.top()]=i;
                ss.pop();
            }
            ss.push(i);
        }
        int ans=0;
        for(int i=0;i<n;i++)
        {
            int l=next[i]-prev[i]-1;
            if(arr[i]<=l)
                ans=max(ans,l);
        }
        return ans;
    }
};