"""
Problem: Next Greater Element
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/next-greater-element/1

Approach:
- For each element in the array, we want to find the next greater element to its right.
- Use a **monotonic decreasing stack** to process elements efficiently:
  - Traverse the array from right to left.
  - While the stack is not empty and the stack’s top is <= current element, pop from the stack.
  - If the stack is not empty, the top is the next greater element for the current element.
  - If the stack is empty, the next greater element is -1.
  - Push the current element onto the stack.
- Return the result array.

Time Complexity: O(n), since each element is pushed and popped from the stack at most once.  
Space Complexity: O(n), for the stack and result array.
"""


class Solution:
    def store(self,arr,total):
        for z in arr:
            total.append(z)

    def nextGreater(self,arr):
        total=[]
        self.store(arr,total)
        self.store(arr,total)
        n=len(total)
        ans=[-1]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and st[-1]<=total[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            else:
                ans[i]=-1
            st.append(total[i])
        arr_n=len(arr)
        res=[]
        for i in range(arr_n):
            res.append(ans[i])
        return res
