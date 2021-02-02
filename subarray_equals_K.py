from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prenum, ans = 0, 0
        dic = Counter()
        # this is very important
        dic[0] = 1
        for i, num in enumerate(nums):
            prenum += num
            left = prenum - k
            ans += dic[left]
            dic[prenum] += 1
        return ans
        

test = Solution()
nums = [1]
k = 0
res = test.subarraySum(nums, k)
print(res)