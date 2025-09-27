/*
Problem: Minimum Number of K Consecutive Bit Flips
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

Approach:
- Goal: Flip minimum number of subarrays of length k to make all elements 1.
- Use a **queue-based sliding window** to track flips efficiently:
  1. `flipped` indicates the current flip state at index `i`.
  2. `queue` stores the indices where flips end (i + k).
  3. For each index `i`:
     - If `queue.front() == i`, pop it and toggle `flipped`.
     - If current bit `arr[i] ^ flipped == 0` (needs flip):
         • If i + k > n → impossible, return -1.
         • Increment `flips`.
         • Push i + k into `queue` to mark the end of this flip.
         • Toggle `flipped`.
- This approach avoids repeatedly flipping the array; the XOR trick maintains the current state.

Time Complexity: O(n), each element is pushed/popped from the queue at most once.  
Space Complexity: O(n), for the queue storing flip-end indices.
*/

class Solution {
    public:
        static int kBitFlips(std::vector<int>& arr, int k) {
            int n = arr.size();
            int flips = 0;
            int flipped = 0;
            std::queue<int> queue;
            for (int i = 0; i < n; i++) {
                if (!queue.empty() && queue.front() == i) {
                    queue.pop();
                    flipped ^= 1;
                }
                if ((arr[i] ^ flipped) == 0) {
                    if (i + k > n) return -1;
                    flips++;
                    queue.push(i + k);
                    flipped ^= 1;
                }
            }
            return flips;
        }
    };