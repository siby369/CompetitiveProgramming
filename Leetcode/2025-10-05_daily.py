"""
Problem: Pacific Atlantic Water Flow
Difficulty: Medium
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Approach:
- Water can flow from a cell to another if the next cell’s height is <= current cell’s height.
- We need cells that can reach both the **Pacific** (top & left edges) and **Atlantic** (bottom & right edges) oceans.
- Instead of simulating water flow *from every cell outward*, we reverse the logic:
  - Perform DFS starting from the ocean edges inward, marking cells reachable from each ocean.
  - For each DFS call:
    - Only move to neighboring cells that are **equal or higher** (since water can flow down from them).
- Finally, find intersection of cells reachable from both oceans.

Steps:
1. Run DFS from all Pacific-border cells (top row and left column).
2. Run DFS from all Atlantic-border cells (bottom row and right column).
3. The intersection of both visited sets gives cells that can reach both oceans.

Time Complexity: O(m * n)
- Each cell is visited at most twice (once per ocean).
Space Complexity: O(m * n)
- For recursion and visited sets.

Key Insight:
- Reverse the flow: Instead of simulating all possible downward paths, climb upward from the oceans — far more efficient.
"""



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(visited, row, col, start_value):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if (row, col) in visited:
                return
            
            if heights[row][col] < start_value:
                return
            
            visited.add((row, col))
            dfs(visited, row+1, col, heights[row][col]) 
            dfs(visited, row-1, col, heights[row][col])
            dfs(visited, row, col+1, heights[row][col])
            dfs(visited, row, col-1, heights[row][col])
            
        for col in range(cols):
            dfs(pacific_visited, 0, col, heights[0][col])
            dfs(atlantic_visited, rows-1, col, heights[rows-1][col])
        
        for row in range(rows):
            dfs(pacific_visited, row, 0, heights[row][0])
            dfs(atlantic_visited, row, cols-1, heights[row][cols-1])
        
        output = [list(cell) for cell in pacific_visited & atlantic_visited]
        return output