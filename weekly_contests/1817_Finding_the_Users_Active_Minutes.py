from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        dir_map = defaultdict(set)
        for i, ele in enumerate(logs):
            dir_map[ele[0]].add(ele[1])
            
        res = [0] * (k + 1)
        for i in dir_map:
            uam = len(dir_map[i])
            res[uam] += 1
        return res[1:]