from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums):

        if len(nums) <= 2:
            return []

        nums = sorted(nums)

        def help(tmp_n, target):
            res = {}
            results = []
            checked = float('inf')
            for i, ele in enumerate(tmp_n):
                if ele == checked:
                    continue
                if ele in res:
                    checked = ele
                    results.append([ele, tmp_n[res[ele]]])
                res[target-ele] = i
            return results
        
        result = []
        checked = float('inf')
        for i, ele in enumerate(nums):
            if ele == checked:
                continue
            if i >= len(nums) - 2:
                break
            checked = ele
            tmp_n = nums[i+1:]
            target = -ele
            
            tmp_res = help(tmp_n, target)
            if tmp_res:
                for t in tmp_res:
                    t.append(ele)
                    result.append(t)
        return result


test = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [0, 0, 0]
# nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
nums = [-2,0,0,2,2]
res = test.threeSum(nums)
print(res)