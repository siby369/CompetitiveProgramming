"""
Problem: Compare Version Numbers
Difficulty: Medium
Link: https://leetcode.com/problems/compare-version-numbers/

Approach:
1. Split both version strings into parts using "." as a delimiter.
   - Example: "1.01" -> ["1", "01"]
2. Convert each part to an integer (removes leading zeros).
3. Iterate up to the maximum length of both version arrays:
   - If one version is shorter, treat missing parts as 0.
   - Compare corresponding parts:
     • If version1[i] < version2[i], return -1
     • If version1[i] > version2[i], return 1
4. If all parts are equal, return 0.

Example:
version1 = "1.01", version2 = "1.001"
- Parts: ["1","01"], ["1","001"]
- Converted: [1,1], [1,1]
- All equal → return 0

version1 = "1.0.1", version2 = "1"
- Parts: ["1","0","1"], ["1"]
- Compare: (1 vs 1), (0 vs 0), (1 vs 0)
- 1 > 0 → return 1

Time Complexity: O(max(m, n)), where m and n are the number of parts in version1 and version2.
Space Complexity: O(m + n), for storing split parts.
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1,vs2=version1.split("."),version2.split(".")
        m,n=len(vs1),len(vs2)
        for i in range(max(m,n)):
            a=int(vs1[i]) if i<m else 0
            b=int(vs2[i]) if i<n else 0
            if a<b:
                return -1
            if a>b:
                return 1
        return 0