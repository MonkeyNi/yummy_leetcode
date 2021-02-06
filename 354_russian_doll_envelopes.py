from typing import List
from bisect import bisect_left


class Solution:
    """
    This is a new version of LIS. The key is how to sort the envelopes
    """
    def maxEnvelopes(self, envelopes: List[List[int]]):
        if not envelopes:
            return 0
        res = []
        envelopes.sort(key=lambda t: (t[0], -t[1]))
        for i, ele in enumerate(envelopes):
            ind = bisect_left(res, ele[1])
            if ind == len(res):
                res.append(ele[1])
            else:
                res[ind] = ele[1]
        return len(res)

test = Solution()
envs = [[5,4],[6,4],[6,7],[2,3]]
res = test.maxEnvelopes(envs)
print(res)

            