from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        
        res = []
        for i in range(len(nums)):
            if not (i+1) in dic:
                res.append(i+1)
        return res
    
test = Solution()
nums = [4,3,2,7,8,2,3,1]
res = test.findDisappearedNumbers(nums)
print(res)