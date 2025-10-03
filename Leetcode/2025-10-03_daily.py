"""
Problem: Trapping Rain Water II
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water-ii/

Approach:
- This is the 2D version of the trapping rain water problem.
- Steps:
  1. Use a min-heap (priority queue) to always process the cell with the smallest height first.
  2. Initialize the heap with all border cells and mark them as visited.
  3. While the heap is not empty:
     - Pop the cell with the lowest height `h`.
     - Check all 4 neighboring cells:
       - If neighbor is unvisited:
         - Mark it as visited.
         - If its height < h, water can be trapped: `res += h - neighbor_height`.
         - Push neighbor into heap with height = max(h, neighbor_height) to maintain water level.
- Continue until all reachable cells are processed.

Time Complexity: O(m * n * log(m * n))
- Each cell is processed once and pushed/popped from the heap.
Space Complexity: O(m * n)
- For the visited matrix and heap.

Key Insight:
- The heap ensures we always expand from the lowest boundary, simulating water rising level by level.
"""


import heapq
class Solution:
    def trapRainWater(self,heightMap):
        m,n=len(heightMap),len(heightMap[0])
        if m<=2 or n<=2:
            return 0
        vis=[[0]*n for i in range(m)]
        pq=[]
        for i in range(m):
            heapq.heappush(pq,(heightMap[i][0],i,0))
            heapq.heappush(pq,(heightMap[i][n-1],i,n-1))
            vis[i][0]=vis[i][n-1]=1
        for j in range(n):
            heapq.heappush(pq,(heightMap[0][j],0,j))
            heapq.heappush(pq,(heightMap[m-1][j],m-1,j))
            vis[0][j]=vis[m-1][j]=1
        res=0
        d=[1,0,-1,0,1]
        while pq:
            h,x,y=heapq.heappop(pq)
            for k in range(4):
                nx,ny=x+d[k],y+d[k+1]
                if 0<=nx<m and 0<=ny<n and not vis[nx][ny]:
                    vis[nx][ny]=1
                    if heightMap[nx][ny]<h:
                        res+=h-heightMap[nx][ny]
                    heapq.heappush(pq,(max(heightMap[nx][ny],h),nx,ny))
        return res

