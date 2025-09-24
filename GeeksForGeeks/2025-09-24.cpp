/*
Problem: Design a MinMax Queue
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/design-minmax-queue/1

Approach:
- Implement a queue that supports:
  1. enqueue(x)
  2. dequeue()
  3. getFront()
  4. getMin()
  5. getMax()

- Data Structures:
  - `q` (queue<int>): standard FIFO queue storing all elements.
  - `minideque` (deque<int>): maintains elements in increasing order to allow O(1) retrieval of minimum.
  - `maxideque` (deque<int>): maintains elements in decreasing order to allow O(1) retrieval of maximum.

- Methods:
  - `enqueue(x)`:
    - Push x to `q`.
    - Pop elements from back of `minideque` while they are greater than x, then push x to back.
    - Pop elements from back of `maxideque` while they are smaller than x, then push x to back.
  - `dequeue()`:
    - Remove front element from `q`.
    - If it matches the front of `minideque` / `maxideque`, pop it from the respective deque.
  - `getFront()`: Return front of `q`.
  - `getMin()`: Return front of `minideque` (minimum element).
  - `getMax()`: Return front of `maxideque` (maximum element).

Time Complexity:
- `enqueue`: O(1) amortized, elements may be pushed/popped from deques at most once.
- `dequeue`: O(1)
- `getFront`, `getMin`, `getMax`: O(1)

Space Complexity:
- O(n), for storing elements in `q`, `minideque`, and `maxideque`.
*/


class SpecialQueue {
  public:
    queue<int>q;
    deque<int>minideque;
    deque<int>maxideque;

    void enqueue(int x) {
        q.push(x);
        while(!minideque.empty() && minideque.back()>x)
        {
            minideque.pop_back();
        }
        minideque.push_back(x);
        while(!maxideque.empty() && maxideque.back()<x)
        {
            maxideque.pop_back();
        }
        maxideque.push_back(x);
    }

    void dequeue() {
        if(q.empty())
        {
            return;
        }
        int frontvalue = q.front();
        q.pop();
        if(!minideque.empty() && minideque.front()==frontvalue)
        {
            minideque.pop_front();
        }
        if(maxideque.front()==frontvalue && !maxideque.empty())
        {
            maxideque.pop_front();
        }
    }

    int getFront() {
        return q.front();
    }

    int getMin() {
        return minideque.front();
    }

    int getMax() {
        return maxideque.front();
    }
};