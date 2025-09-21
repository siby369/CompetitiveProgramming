"""
Problem: Max Rectangle in Binary Matrix
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/max-rectangle/1

Approach:
- The problem is to find the largest rectangle containing only 1's in a binary matrix.
- Treat each row as the base of a histogram:
  - `bars[j]` stores the number of consecutive 1's in column `j` up to the current row.
- For each row, compute the largest rectangle area in the histogram:
  - Use monotonic stacks to compute:
    - `pse[i]`: Previous Smaller Element index for bars[i].
    - `nse[i]`: Next Smaller Element index for bars[i].
  - Rectangle width for `bars[i]` = `nse[i] - pse[i] - 1`.
  - Area = `bars[i] * width`.
- Update the maximum area across all rows.

Time Complexity:
- O(n * m), where n = number of rows, m = number of columns.
  - Each row is processed in O(m) time using stacks.

Space Complexity:
- O(m), for `pse`, `nse`, and the stack for each row.

"""


class Solution:
    def getArea(self, m, bars):
        nse=[m]*m
        pse=[-1]*m
        st=[]
        for i in range(m):
            while st and bars[st[-1]]>=bars[i]:
                st.pop()
            if st:
                pse[i]=st[-1]
            st.append(i)
        st.clear()
        for i in range(m-1,-1,-1):
            while st and bars[st[-1]]>=bars[i]:
                st.pop()
            if st:
                nse[i]=st[-1]
            st.append(i)
        area=0
        for i in range(m):
            area=max(area,bars[i]*(nse[i]-pse[i]-1))
        return area

    def maxArea(self, mat):
        n=len(mat)
        m=len(mat[0])
        ans=0
        bars=[0]*m
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    bars[j]=0
                else:
                    bars[j]+=1
            ans=max(ans,self.getArea(m,bars))
        return ans
