from bisect import bisect_left as bl
class Solution:
    def increasingTriplet(self, nums):
        if len(nums) <= 2:
            return False
        
        res = []
        for i, ele in enumerate(nums):
            ind = bl(res, ele)
            if ind == len(res):
                res.append(ele)
            else:
                res[ind] = ele
            if len(res) == 3:
                print(res)
                return True
        return False

test = Solution()
nums = [5,4,3,2,1]
res = test.increasingTriplet(nums)
print(res)
