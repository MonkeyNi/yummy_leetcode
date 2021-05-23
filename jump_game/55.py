from collections import deque

class Solution:
    """
    Greedy solution. MinJump = 0, MaxJump = nums[i].
    For each step, we only need to record max ind that we can reach;
    """
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

test = Solution()
nums = [2, 3, 1, 1, 4]
# nums = [1, 1, 1, 0]
nums = [3, 2, 1, 0, 4]
nums = [3, 0, 8, 2, 0, 0, 1]

res = test.canJump(nums)
print(res)