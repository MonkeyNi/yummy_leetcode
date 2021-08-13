class Solution:
    """
    Brilliant solution
    https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space
    """
    def maxSumDivThree(self, nums):
        dp = [0, 0, 0]
        for n in nums:
            for i in dp[:]:  # copy of array
                dp[(i+n)%3] = max(dp[(i+n)%3], i+n)
        return dp[0]
        
        