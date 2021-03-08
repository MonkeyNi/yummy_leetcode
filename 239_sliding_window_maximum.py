from typing import List
from collections import deque


class Solution:
    """
    By using 'deque', insert or delete can be completed in O(1) time complexity.
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if not nums:
        #     return []
        
        # if len(nums) <= k:
        #     return [max(nums)]

        # res = []
        # for i in range(len(nums) - k + 1):
        #     res.append(max(nums[i:i+k]))  # max/min: O(n)
        # return res
        
        if not nums:
            return []
        
        res = []
        queue = deque()
        for i, ele in enumerate(nums):
            while queue and ele > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            if queue[0] + k == i:
                queue.popleft()
                
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
    
    

test = Solution()
nums = [5,3,4]
k = 1
res = test.maxSlidingWindow(nums, k)
print(res)