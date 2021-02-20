from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        
        res = []
        for i in range(len(nums)):
            if not (i+1) in dic:
                res.append(i+1)
        return res
    
    def findDisappearedNumbers_2(self, nums: List[int]):
        nums.sort()
        res = []

        i = 0
        for n in nums:
            if (i+1)^n == 0:
                i += 1
            elif (i+1) < n:
                res.extend([a for a in range(i+1, n)])
                i = n
        if i != len(nums):
            res.extend([a for a in range(i+1, len(nums)+1)])
        return res
            

test = Solution()
nums = [4,3,2,7,8,2,3,1]
# nums = [1, 1]
# nums = [4,3,2,7,7,2,3,1]
res = test.findDisappearedNumbers_2(nums)
# res = test.findDisappearedNumbers(nums)
print(res)