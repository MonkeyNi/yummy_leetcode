from typing import List


class Solution:
    """
    dp[i]: 在第i间房，可以最多抢到的数量
    选择：抢或者不抢
    状态：第几间房子
    """
    def rob(self, nums: List[int]):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums)-1]

    def rob_2(self, nums: List[int]):
        if not nums:
            return 0
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
nums = [1,2,3,1]
# nums = [2,7,9,3,1]
# nums = [2,1,1,2]
res = test.rob_2(nums)
print(res)