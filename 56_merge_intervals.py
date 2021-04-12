from typing import List


class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        # sort by start
        sort_int = sorted(intervals, key=lambda x:x[0])
        res = [sort_int[0]]

        for i in range(1, len(sort_int)):
            cur = sort_int[i]

            last = res[-1]
            if cur[0] <= last[1]:
                last[1] = max(cur[1], last[1])
            else:
                res.append(cur)
        return res


test = Solution()
intervals = [[1,4],[4,5]]
res = test.merge(intervals)
print(res)
        