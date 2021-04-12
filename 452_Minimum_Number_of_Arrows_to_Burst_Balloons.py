class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        sort_int = sorted(points, key=lambda x: x[1])

        res = 1
        end = sort_int[0][1]
        for inter in sort_int[1:]:
            if inter[0] > end:
                res += 1
                end = inter[1]
        return res

test = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
res = test.findMinArrowShots(points)
print(res)
        