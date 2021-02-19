from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # print(nums)
        return slow+1
    
    
test = Solution()
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = []
res = test.removeDuplicates(nums)
print(res)