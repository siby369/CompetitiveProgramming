"""
Problem: Water Bottles
Difficulty: Easy
Link: https://leetcode.com/problems/water-bottles/

Approach:
- You start with `numBottles` full water bottles.
- After drinking a bottle, the empty bottle can be exchanged:
  - `numExchange` empty bottles → 1 full bottle.
- Steps:
  1. Initialize `drinked = 0` (total bottles consumed), `eb = 0` (empty bottles).
  2. While there are bottles to drink:
     - Drink all current bottles: add `numBottles` to `drinked`.
     - Add the consumed bottles to empty bottle count `eb`.
     - Exchange empty bottles: `numBottles = eb // numExchange`.
     - Keep remainder empty bottles: `eb = eb % numExchange`.
  3. Repeat until no more bottles can be obtained.
- Return `drinked` as the total number of bottles consumed.

Time Complexity: O(log numBottles)
- Each iteration reduces the effective number of bottles by the exchange factor.
Space Complexity: O(1)
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked,eb=0,0
        while numBottles>0:
            drinked+=numBottles
            eb+=numBottles
            numBottles=eb//numExchange
            eb=eb%numExchange
        return drinked