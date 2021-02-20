from typing import List


class Solution:
    """
    利用索引与元素一一对应的关系，给‘映射’到的元素进行符号转换（标记）
    """
    def findErrorNums(self, nums: List[int]):
        if not nums:
            return []
        
        dup, miss = 0, 0
        for i, ele in enumerate(nums):
            ele = abs(ele) # abs! this mean index which should be positive
            if nums[ele-1] < 0:
                dup = abs(nums[i]) # abs! this mean duplicate number which should be positive
            else:
                nums[ele-1] *= -1

        for i, ele in enumerate(nums):
            if ele > 0:
                miss = i + 1
        return [dup, miss]


test = Solution()
nums = [1,2,2,4]
# nums = [1,1]
# nums = [2, 2]
res = test.findErrorNums(nums)
print(res)
