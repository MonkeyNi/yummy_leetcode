class Solution():
    def rob(self, nums):
        """
        1 <= nums.length <= 100
        0 <= nums[i] <= 400

        Idea: for the ith house, there are two situations
            1. robbed: dp[i] = dp[i-2] + nums[i]
            2. not robbed: dp[i] = dp[i-1]

        Optimization: since dp_i is only related to two previous status,
            so we just need two variables instead of dp array.
        """
        if len(nums) <= 2:
            return max(nums)
        dp_0 = nums[0]
        dp_1 = max(dp_0, nums[1])
        for i in range(2, len(nums)):
            dp_0, dp_1 = dp_1, max(dp_0+nums[i], dp_1)
        return dp_1
