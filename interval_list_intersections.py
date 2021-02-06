from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]):
        if not firstList or not secondList:
            return []
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            if a1 <= b2 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])
            if a2 > b2:
                j += 1
            else:
                i += 1
        return res


test = Solution()
firstList = [[1,7]]
secondList = [[3,10]]
res = test.intervalIntersection(firstList, secondList)
print(res)
