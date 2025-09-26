/*
Problem: Rotate Deque by K
Difficulty: Easy
Link: https://www.geeksforgeeks.org/problems/rotate-deque-by-k/1

Approach:
- Rotate a deque `dq` either left or right by `k` positions.
- Parameters:
  - `dq`: deque to rotate
  - `type`: 0 → rotate left, 1 → rotate right
  - `k`: number of positions to rotate
- Steps:
  1. Take modulo with deque size: `k = k % dq.size()`.
  2. If right rotation (`type == 1`), convert it to equivalent left rotation:
     - `k = dq.size() - k`
  3. Perform left rotation `k` times:
     - Pop front element and push it to back.

Time Complexity: O(k) – each rotation moves one element.  
Space Complexity: O(1) – in-place rotation.
*/

class Solution {
    public:
      void rotateDeque(deque<int>& dq, int type, int k) {
          k = k%dq.size();
          int i;
          if(type == 1)
          {
              k=dq.size()-k;
          }
          for(i=0;i<k;i++)
          {
              int temp = dq.front();
              dq.pop_front();
              dq.push_back(temp);
          }
      }
  };