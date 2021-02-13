from bisect import bisect_left
from typing import List


class Solution:
    # 纸牌游戏的思路，利用二分法， O(N) = O(nlogn)
    def lengthOfLIS_binary(self, nums: List[int]):
        if not nums:
            return []
        res = []
        for i, ele in enumerate(nums):
            ind = bisect_left(res, ele)
            if ind == len(res):
                res.append(ele)
            else:
                res[ind] = ele

        return len(res)

    # 动态规划的思路，数学归纳法， O(N) = O(n^2)
    def lengthOfLIS_dp(self, nums: List[int]):
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


test = Solution()
nums = [0,1,0,3,2,3]
res = test.lengthOfLIS_binary(nums)
res = test.lengthOfLIS_dp(nums)
print(res)