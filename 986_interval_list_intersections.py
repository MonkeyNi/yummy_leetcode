class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []
        
        res = []
        n = len(firstList)
        m = len(secondList)
        i, j = 0, 0
        while i < n and j < m:
            a = firstList[i]
            b = secondList[j]
            if b[0] <= a[1] and a[0] <= b[1]:
                res.append([max(a[0], b[0]), min(a[1], b[1])])
            
            # pay attention to the if condition
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        return res 


test = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
res = test.intervalIntersection(firstList, secondList)
print(res)
        