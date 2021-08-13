from typing import List


class Solution:
    """
    Note: do not use element as key (maybe duplicate element and it will not be the first samll element)
    """
    def nextGreaterElements(self, nums: List[int]):
        if not nums:
            return []
        # initialization
        res = [-1]*len(nums)
        stack = []
        for i in range(2*len(nums)):
            ci = i%len(nums)
            while stack and nums[ci] > nums[stack[-1]]:
                res[stack.pop()] = nums[ci]
            stack.append(ci) 
        return res


test = Solution()
nums = [1, 2, 1]
res = test.nextGreaterElements(nums)
print(res)