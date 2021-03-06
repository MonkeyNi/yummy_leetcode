from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]):
        if not T:
            return []

        res = [0]*len(T)
        stack = []
        for i, ele in enumerate(T):
            while stack and ele > T[stack[-1]]:
                t = stack.pop()
                res[t] = i - t
            stack.append(i)
        return res

    
test = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
res = test.dailyTemperatures(T)
print(res)