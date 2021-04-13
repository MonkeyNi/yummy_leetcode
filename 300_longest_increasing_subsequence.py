from bisect import bisect_left as bl


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return 1
        
        res = [nums[0]]
        for i, ele in enumerate(nums[1:]):
            ind = bl(res, ele)
            if ind == len(res):
                res.append(ele)
            else:
                res[ind] = ele

        return len(res)

test = Solution()
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
res = test.lengthOfLIS(nums)
print(res)

        