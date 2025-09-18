"""
Problem: 2290. Design Task Manager
Difficulty: Hard
Link: https://leetcode.com/problems/design-task-manager/

Approach:
- Use a hash map (`mp`) to store active tasks, mapping `taskId` → (priority, userId).
- Use a max-heap (`pq`) to efficiently fetch the highest-priority task.
  - Store elements as (-priority, -taskId) to simulate max-heap with Python’s `heapq` (which is min-heap).
- Methods:
  - `__init__`: Initialize the manager with given tasks, pushing them into both `mp` and `pq`.
  - `add`: Insert a new task into both `mp` and `pq`.
  - `edit`: Update the priority of an existing task. Push the new (priority, taskId) into the heap. (Lazy deletion ensures outdated entries are ignored later.)
  - `rmv`: Remove a task by deleting it from `mp` (outdated copies in the heap will be skipped later).
  - `execTop`: Continuously pop from the heap until finding a valid entry still present in `mp` with matching priority.
    - Return the corresponding `userId` and remove the task.
    - If no valid task remains, return -1.

Time Complexity:
- `add` / `edit` / `rmv`: O(log n) for heap push, O(1) for hashmap updates.
- `execTop`: Amortized O(log n), since each task is pushed and popped at most once.

Space Complexity: O(n), for storing tasks in both the hashmap and heap.
"""



class TaskManager:
    def __init__(self,tasks:List[List[int]]):
        self.mp:dict[int,tuple[int,int]]={}
        self.pq:list[tuple[int,int]]=[]
        for u,i,p in tasks:
            self.mp[i]=(p,u)
            heapq.heappush(self.pq,(-p,-i))

    def add(self,userId:int,taskId:int,priority:int)->None:
        self.mp[taskId]=(priority,userId)
        heapq.heappush(self.pq,(-priority,-taskId))

    def edit(self,taskId:int,newPriority:int)->None:
        if taskId in self.mp:
            u=self.mp[taskId][1]
            self.mp[taskId]=(newPriority,u)
            heapq.heappush(self.pq,(-newPriority,-taskId))

    def rmv(self,taskId:int)->None:
        self.mp.pop(taskId,None)

    def execTop(self)->int:
        while self.pq:
            negp,neg_tid=heapq.heappop(self.pq)
            p,tid=-negp,-neg_tid
            if tid in self.mp and self.mp[tid][0]==p:
                u=self.mp[tid][1]
                del self.mp[tid]
                return u
        return -1
