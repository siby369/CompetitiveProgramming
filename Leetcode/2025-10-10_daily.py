"""
Problem: Maximum Energy Boost from Jumping
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-energy-boost-from-jumping/

Approach:
- You are given an array `energy`, where `energy[i]` represents the energy gained at position `i`.
- You can start from any index and move forward by exactly `k` steps repeatedly.
- The goal is to find the **maximum total energy** you can accumulate by following such jumps.

Intuition:
- Starting from the end, we can compute the maximum energy obtainable if you start at each position.
- For every index `i`, the total energy is:
    `dp[i] = energy[i] + dp[i + k]` (if `i + k` is within bounds)
- Otherwise, if jumping out of bounds, `dp[i] = energy[i]`.
- We initialize `dp` as a copy of `energy`, then update values from right to left.
- Finally, return the maximum value in `dp` — the best possible starting position.

Steps:
1. Copy the array: `dp = energy[:]`
2. Traverse from `len(energy) - k - 1` down to `0`
   - Add energy from the cell `i + k` (future reachable cell).
3. Return `max(dp)` since you can start from any valid index.

Example:
Input:
energy = [5,2,-10,-5,1], k = 3

Computation:
dp = [5,2,-10,-5,1]
Start from i = 1 (since len=5, k=3 → 5-3-1=1)
i=1 → dp[1] += dp[4] → 2+1=3
i=0 → dp[0] += dp[3] → 5+(-5)=0
dp = [0,3,-10,-5,1]

Maximum = 3 → Best starting at index 1

Output:
3

Time Complexity: O(n)
- Single backward pass through the array.
Space Complexity: O(n)
- For storing the dp array (can be optimized to O(1) with in-place updates).

Key Insight:
- The problem is a **1D dynamic programming** variant where future states are spaced `k` apart.
- Traversing backward ensures all dependent states (`i + k`) are already computed.
"""

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[:]
        for i in range(len(energy) - k - 1, -1, - 1):
            dp[i] += dp[i + k]
        return max(dp)