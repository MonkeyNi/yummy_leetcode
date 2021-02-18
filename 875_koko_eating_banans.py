from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if not piles:
            return 0
        end = max(piles)
        start = 1 # instead of 0
        while start <= end:
            mid = int(start + (end - start) / 2)
            time_limit = sum([math.ceil(float(p)/mid) for p in piles])
            if time_limit > H:
                start = mid + 1 
            else:
                end = mid - 1
   
        if end != 0 and sum([math.ceil(p/end) for p in piles]) <= H:
            return end
        else:
            return start
        

test = Solution()
piles = [3,6,7,11]
H = 8
piles = [30,11,23,4,20]
H = 5
piles = [30,11,23,4,20]
H = 6
piles = [312884470]
H = 968709470
# piles = [2, 2]
# H = 2
res = test.minEatingSpeed(piles, H)
print(res)