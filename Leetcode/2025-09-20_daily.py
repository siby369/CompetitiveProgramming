"""
Problem: Implement Router
Difficulty: Medium
Link: https://leetcode.com/problems/implement-router/description/

Approach:
- Simulate a router with limited memory that stores packets and allows packet forwarding and querying.
- Use the following data structures:
  - `q` (deque): Keeps packets in arrival order for FIFO operations.
  - `dts` (defaultdict of deques): Maps each destination to a sorted list of timestamps for fast range queries.
  - `seen` (set): Tracks existing packets to avoid duplicates.
- Methods:
  - `addPacket(source, destination, timestamp) -> bool`:
    - Adds a packet if it does not exist already.
    - If memory exceeds the capacity, evict the oldest packet.
    - Returns `True` if added, else `False`.
  - `forwardPacket() -> List[int]`:
    - Pops the oldest packet and returns `[source, destination, timestamp]`.
    - Returns `[]` if no packet exists.
  - `getCount(destination, startTime, endTime) -> int`:
    - Counts packets for a destination whose timestamps lie within `[startTime, endTime]` using binary search.

Time Complexity:
- `addPacket`: O(1) amortized for append/pop operations.
- `forwardPacket`: O(1).
- `getCount`: O(log n), using `bisect` on destination timestamps.

Space Complexity: O(capacity), storing at most `capacity` packets in memory.
"""


class Router:

    def __init__(self, memoryLimit: int):
        self.cap=memoryLimit
        self.q=deque()
        self.dts=defaultdict(deque)
        self.seen=set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.seen:
            return False
        self.q.append((source,destination,timestamp))
        self.dts[destination].append(timestamp)
        self.seen.add((source,destination,timestamp))
        if len(self.q)>self.cap:
            pack=self.q.popleft()
            des=pack[1]
            self.dts[des].popleft()
            self.seen.discard(pack)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s,d,t=self.q.popleft()
        self.dts[d].popleft()
        self.seen.discard((s,d,t))
        return [s,d,t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left=bisect.bisect_left(self.dts[destination],startTime)
        right=bisect.bisect_right(self.dts[destination],endTime)
        return right-left
