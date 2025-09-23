"""
Problem: Queue Reversal
Difficulty: Easy
Link: https://www.geeksforgeeks.org/problems/queue-reversal/1

Approach:
1. The task is to reverse the order of elements in a queue.
2. Use recursion:
   - Base case: If the queue is empty, return.
   - Recursive case:
     • Remove (popleft) the front element.
     • Recursively reverse the remaining queue.
     • Append the removed element to the rear.
3. This effectively pushes each element to the back after the recursive call,
   achieving a reversed order.

Example:
Queue = [1, 2, 3, 4, 5]
- Remove 1 → reverse [2, 3, 4, 5]
- Remove 2 → reverse [3, 4, 5]
- ...
- Final reversed queue = [5, 4, 3, 2, 1]

Time Complexity: O(n) – each element is enqueued and dequeued once.
Space Complexity: O(n) – due to recursive call stack.

Alternative:
- Can also be solved iteratively using a stack.
"""

class Solution:
    def reverseQueue(self, q):
        if not q:
            return 
        f=q.popleft()
        self.reverseQueue(q)
        q.append(f)