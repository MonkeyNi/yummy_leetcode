from typing import List


class Solution:
    """
    suppose that sum(+) = A and sum(-) = B, then
    sum(nums) = A +B
    target = A - B
    so, A = (sum(nums)+target) / 2.
    We need to find the number of solutions.
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # note that target can be negative
        if target > sum(nums) or -target > sum(nums):
            return 0
        
        target = abs(sum(nums) + target)
        if target % 2:
            return 0
        else:
            target //= 2
        
        dp = [1] + [0]*target  # dp[0]=1, why
        for n in nums:
            for t in range(target, -1, -1):  # not (target, 0, -1)
                if t - n >= 0:
                    dp[t] = dp[t] + dp[t-n]
        return dp[target]
    