"""
Problem: Maximum Total Damage
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-total-damage/

Approach:
- You are given an array `power`, where each element represents the damage value of a weapon type.
- If you choose a weapon with power `x`, you **cannot** choose weapons with power `x-2`, `x-1`, `x+1`, or `x+2`.
- The goal is to maximize the total sum of selected weapons’ power values.

Intuition:
- This problem is similar to the **House Robber** or **Delete and Earn** pattern:
  - Taking one value invalidates taking nearby ones (within a distance of 2).
- We first compress the input:
  - Count frequency of each unique power value using `Counter()`.
  - Sort the unique keys.

Dynamic Programming Relation:
- Let `dp[i]` be the maximum total damage considering weapon powers up to `keys[i]`.
- Two choices for each index:
  1. **Skip** current power → `dp[i] = dp[i-1]`
  2. **Take** current power → total = `freq[keys[i]] * keys[i] + dp[j]`
     where `j` is the **latest index** such that `keys[j] <= keys[i] - 3`  
     (ensuring no overlap rule violation).

We find `j` efficiently using **binary search**, since `keys` is sorted.

Transition:
dp[i] = max(dp[i-1], freq[keys[i]] * keys[i] + dp[j])

Steps:
1. Count frequency of each unique power using `Counter`.
2. Sort all unique keys.
3. Initialize `dp[0] = freq[keys[0]] * keys[0]`.
4. For each `i` from 1 to n-1:
   - Use binary search to find the last valid index `ans` where `keys[ans] <= keys[i] - 3`.
   - Update `dp[i] = max(dp[i-1], freq[keys[i]] * keys[i] + dp[ans])`.
5. Return `dp[-1]`.

Example:
Input:
power = [2,5,3,5,2]

Frequency Map:
{2:2, 3:1, 5:2}
Keys = [2,3,5]

DP:
dp[0] = 4  (2*2)
dp[1] = max(4, 3*1) = 4
dp[2] = max(4, 5*2 + dp[0]) = 14
Output = 14

Explanation:
Choose power 2 and 5 → total damage = 4 + 10 = 14.

Time Complexity: O(n log n)
- O(n log n) for sorting and binary search per iteration.
Space Complexity: O(n)
- For dp and frequency arrays.

Key Insight:
- The problem generalizes the “Delete and Earn” DP.
- Binary search efficiently finds the latest non-conflicting weapon index.
"""
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]
        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            l, r, ans = 0, i - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if keys[mid] <= keys[i] - 3:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if ans >= 0:
                take += dp[ans]
            dp[i] = max(dp[i - 1], take)
        return dp[-1]