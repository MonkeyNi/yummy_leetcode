from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]):
        if not target:
            return 0

        start = end = i = 0
        tmp = 0  # slide window sum
        for j, ele in enumerate(nums, start=1):
            tmp += ele
            if tmp >= target:
                while i < j and tmp-nums[i] >= target:
                    tmp -= nums[i]
                    i += 1
                if not end or j-i < end-start:
                    start, end = i, j
        return end-start


test = Solution()
target = 7
nums = [2,3,1,2,4,3]
target = 4
nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
res = test.minSubArrayLen(target, nums)
print(res)
