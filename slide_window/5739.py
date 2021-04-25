class Solution:
    """
    这个问题实际上就是找符合条件的最长子序列，记录最长长度就可以
    Sliding window, O(n)
    """
    def maxFrequency(self, nums, k):
        if not nums:
            0
        nums = sorted(nums)
        res = 1
        start = 0
        for end in range(len(nums)):
            k += nums[end]
            if k < nums[end] * (end-start+1):
                k -= nums[start]
                start += 1
            res = max(res, end-start+1)
        return res
       

test = Solution()
nums = [1,2,4]
k = 5
nums = [1,4,8,13]
k = 5
nums = [3,9,6]
k = 2
res = test.maxFrequency(nums, k)
print(res)