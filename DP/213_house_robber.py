from typing import List


class Solution:
    """
    dp[i]: 在第i间房，可以最多抢到的数量
    选择：抢或者不抢
    状态：第几间房子
    Note: 异常判断
    """
    def rob(self, nums: List[int]):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.help(nums[:-1]), self.help(nums[1:]))

    def help(self, nums: List[int]):
        if len(nums) <= 2:
            return max(nums)
        dp_0 = nums[0]
        dp_1 = max(nums[:2])
        for i in range(2, len(nums)):
            res = max(dp_0 + nums[i], dp_1)
            dp_0 = dp_1
            dp_1 = res
        return res

test = Solution()
nums = [2,3,2]
nums = [1,2,3,1]
nums = [1]
res = test.rob(nums)
print(res)