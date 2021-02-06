from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]):
        if not intervals:
            return []
        # This is the key, sort by 'start'
        intervals.sort(key=lambda inter:inter[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]
            if last[1] >= cur[0]:
                last[1] = max(cur[1], last[1])
            else:
                res.append(cur)
        return res

test = Solution()
intervals = [[1,4],[4,5]]
res = test.merge(intervals)
print(res)