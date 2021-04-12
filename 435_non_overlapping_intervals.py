class Solution:
    """
    Greedy problem
    """
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 1

        # chaoose events which will end first
        sort_int = sorted(intervals, key=lambda x:x[1])

        res = 1
        end = sort_int[0][1]
        for inter in sort_int[1:]:
            # no overlap means new event
            if inter[0] >= end:
                res += 1
                end = inter[1]
        return len(intervals) - res
        

test = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
res = test.eraseOverlapIntervals(intervals)
print(res)
        