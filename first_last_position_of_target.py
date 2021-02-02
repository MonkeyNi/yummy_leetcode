from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left(nums, target), self.right(nums, target)]

    def left(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        if l >= len(nums) or nums[l] != target:
            return -1
        return l
    
    def right(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        
        if r < 0 or nums[r] != target:
            return -1
        return r


test = Solution()
nums, target = [5,7,7,8,8,10], 8
res = test.searchRange(nums, target)
print(res)