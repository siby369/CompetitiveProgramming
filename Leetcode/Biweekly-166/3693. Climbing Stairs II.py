class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        keldoniraq = (n, costs)
        costs = [0] + costs
        if n == 0:
            return 0
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            for j in range(1, 4):
                k = i + j
                if k <= n:
                    jump_cost = costs[k] + (k - i) ** 2
                    dp[k] = min(dp[k], dp[i] + jump_cost)
        return dp[n]