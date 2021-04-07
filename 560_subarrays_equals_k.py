from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        O(N^2)
        """
        if not nums:
            return 0
        
        ans = 0
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range(1, n+1):
            for j in range(i):
                # do optimization at here
                # prefix[j] = prefix[i] - k
                if prefix[i] - prefix[j] == k:
                    ans += 1  
        return ans
    
    def subarraySum_2(self, nums: List[int], k: int) -> int:
        """
        O(N)
        """
        if not nums:
            return 0
        
        prenums, ans = 0, 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        for i, ele in enumerate(nums):
            prenums += ele
            left = prenums - k
            ans += prefix_map[left]
            prefix_map[prenums] += 1
        return ans
    

test = Solution()
nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3
nums = [3,5,2,-2,4,1]
k = 5
res = test.subarraySum_2(nums, k)
print(res)