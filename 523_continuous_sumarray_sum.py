from typing import List
from collections import defaultdict
from itertools import accumulate
    

class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            for a, b in zip(nums, nums[1:]):
                if a == 0 and b == 0:
                    return True
            return False
        
        mods, prefix = {0: -1}, 0
        for i, n in enumerate(nums):
            prefix = (prefix + n) % k
            if prefix in mods and i - mods[prefix] > 1:
                return True
            if prefix not in mods:
                mods[prefix] = i
        return False
    
    
test = Solution()
nums = [23,2,4,6,7]
k = 6
nums = [5, 0, 0, 0]
k = 3
res = test.checkSubarraySum(nums, k)
print(res)