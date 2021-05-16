from collections import Counter
from itertools import accumulate


class Solution:
    """
    More thoughts...
    """
    def sumOfFlooredPairs(self, nums):
        nd = Counter(nums)
        inds = [0]*(max(nums)+1)
        
        # key part
        for n in nd:
            for i in range(n, len(inds), n):
                inds[i] += nd[n]
        pren = list(accumulate(inds))

        return int(sum([pren[n]*nd[n] for n in nd])%(10**9+7))


test = Solution()
nums = [7,7,7,7,7,7,7]
# nums = [2,5,9]
res = test.sumOfFlooredPairs(nums)
print(res)