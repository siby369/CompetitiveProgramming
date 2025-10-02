"""
Problem: Max Bottles Drunk
Difficulty: Medium
Link: https://leetcode.com/problems/max-bottles-drunk/

Approach:
- You start with `numBottles` full bottles. After drinking, the empty bottles can be exchanged.
- Unlike the simpler version, here the exchange rate `numExchange` increases by 1 after each successful exchange.
- Steps:
  1. Initialize:
     - `drunk = numBottles` → total bottles consumed.
     - `empty = numBottles` → empty bottles available for exchange.
  2. While you have enough empty bottles (`empty >= numExchange`):
     - Exchange `numExchange` empties for 1 new full bottle.
     - Increment `drunk` by 1 (drinking the new bottle).
     - After drinking, update empties:
       - You spent `numExchange` empties, gained 1 empty back from drinking.
       - So effectively `empty -= numExchange - 1`.
     - Increase exchange requirement: `numExchange += 1`.
  3. Repeat until you cannot exchange further.
  4. Return `drunk`.

Time Complexity: O(n) in worst case, bounded by number of exchanges possible.
Space Complexity: O(1).
"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        while empty >= numExchange:
            drunk += 1
            empty -= numExchange - 1
            numExchange += 1
        return drunk