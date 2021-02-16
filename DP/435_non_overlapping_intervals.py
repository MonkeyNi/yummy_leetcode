from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # sort by end
        intervals.sort(key=lambda x:x[-1])
        
        res = 1
        base = intervals[0]
        for i in range(1, len(intervals)):
            # no overlap if and only if next.start >= pre.end
            if intervals[i][0] >= base[1]:
                res += 1
                base = intervals[i]
        return len(intervals) - res
        

test = Solution()
intervals = [[1,2],[2,3]]
res = test.eraseOverlapIntervals(intervals)
print(res)