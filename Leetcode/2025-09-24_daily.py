"""
Problem: Fraction to Recurring Decimal
Difficulty: Medium
Link: https://leetcode.com/problems/fraction-to-recurring-decimal/

Approach:
1. Handle the sign:
   - If numerator == 0 → return "0".
   - If numerator and denominator have opposite signs, prepend "-".

2. Integer part:
   - Divide numerator by denominator → append quotient to result.
   - Compute remainder.

3. Decimal part:
   - If remainder == 0 → return integer part only.
   - Otherwise, append "." and start simulating long division.

4. Detect cycles (recurring decimals):
   - Use a hashmap `seen` to store each remainder and its position in the result.
   - If the same remainder appears again, we have found a repeating cycle.
   - Insert "(" at the stored index and append ")" at the end.

5. Edge cases:
   - Negative fractions.
   - Fractions that result in terminating decimals (e.g., 1/2 = 0.5).
   - Fractions that result in repeating decimals (e.g., 2/3 = 0.(6)).

Example:
Input: numerator = 4, denominator = 333
Output: "0.(012)"

Time Complexity: O(n) where n = length of repeating cycle (at most denominator).
Space Complexity: O(n) for storing remainders in hashmap.

Alternative:
- Some implementations build the decimal part in a separate list 
  and only join once at the end to reduce insert operations.
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        n = abs(numerator)
        d = abs(denominator)
        res.append(str(n // d))
        rem = n % d
        if rem == 0:
            return ''.join(res)
        res.append('.')
        seen = {}
        while rem:
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, '(')
                res.append(')')
                break
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem = rem % d
        return ''.join(res)