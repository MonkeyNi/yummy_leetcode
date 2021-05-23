class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        res = 1 # if we set r=nums[0], res=1, elif r=0,res=0
        l, r = 0, nums[0]
        # we do not need to consider the last ele in nums, since  r>= len(nums)-1
        while r < len(nums)-1:
            res += 1
            nxt = max(i+nums[i] for i in range(l, r+1))
            l, r = r, nxt
        return res

test = Solution()
nums = [2, 3, 1, 1, 4]
res = test.jump(nums)
print(res)