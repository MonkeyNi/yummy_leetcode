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
        # dp_0, dp_1, dp_2 (res)
        # when calculate dp_2, there are two situations
        #   1. inlcude dp_1, which is dp_1
        #   2. not include dp_1, which is dp_0 + dp_2
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

    def rob_3(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = nums[0]
        for i in range(1, n):
            num = nums[i]
            dp[i][1] = dp[i-1][0] + num
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            
        return max(dp[n-1])

test = Solution()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
# nums = [2,1,1,2]
res = test.rob_3(nums)
print(res)