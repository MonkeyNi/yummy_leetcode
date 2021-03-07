from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]):
        res = 0
        heights.append(0)  # deal with monotonic increasing situation, dummy bar
        stack = [-1] # ? dummy ind
        for i, ele in enumerate(heights):
            # find next smaller bar, keep ascending in the stack
            while stack and ele < heights[stack[-1]]:
                h = heights[stack.pop()]
                # count rectangle with height h
                # right boundary: stack[-1]
                # left boundary: i
                w = i - stack[-1] - 1  # cannot count left and right boundary
                res = max(res, h*w)
            stack.append(i)
        return res


test = Solution()
heights = [2,1,5,6,2,3]
res = test.largestRectangleArea(heights)
print(res)
        