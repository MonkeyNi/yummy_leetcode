from math import sqrt
from collections import deque

# BFS 

class Solution:
    def numSquares(self, n: int) -> int:
        end =  int(sqrt(n))
        choose = [i**2 for i in range(1, end+1)]
        queue = deque([(n, 0)])  # target, and number
        visited = {n}  # essential!
        while queue:
            t, num = queue.popleft()
            if t == 0:
                return num
            for cho in choose:
                diff = t - cho
                if diff >= 0 and diff not in visited:
                    queue.append((diff, num+1))
                    visited.add(diff)
        return -1  # impossible...


test = Solution()
n = 13
ans = test.numSquares(n)
print(f'Perfect ans is : {ans}') 