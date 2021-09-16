"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# BFS 

from collections import deque
from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e_dic = {e.id:e for e in employees}
        queue = deque([(id, e_dic[id].importance)])
        ans = 0
        while queue:
            ce, im = queue.popleft()
            ans += im
            subs = e_dic[ce].subordinates
            for s in subs:
                queue.append((s, e_dic[s].importance))
        return ans
