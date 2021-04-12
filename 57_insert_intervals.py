class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
            
        intervals.append(newInterval)
        sort_int = sorted(intervals, key=lambda x:x[0])
        res = [sort_int[0]]
        for inter in sort_int[1:]:
            if inter[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter)
        return res

test = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
res = test.insert(intervals, newInterval)
print(res)


        

        