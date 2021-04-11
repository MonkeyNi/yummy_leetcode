from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]):
        t = len(obstacles)
        dp = [[float('inf') for _ in range(3)] for _ in range(len(obstacles))]
        dp[0][1] = 0
        dp[0][0] = 1
        dp[0][2] = 1

        for i in range(1, t):
            if obstacles[i] != 1:
                dp[i][0] = dp[i-1][0]
            if obstacles[i] != 2:
                dp[i][1] = dp[i-1][1]
            if obstacles[i] != 3:
                dp[i][2] = dp[i-1][2]
            if obstacles[i] != 1:
                dp[i][0] = min(dp[i][0], min(dp[i][1], dp[i][2]) + 1)
            if obstacles[i] != 2:
                dp[i][1] = min(dp[i][1], min(dp[i][0], dp[i][2]) + 1)
            if obstacles[i] != 3:
                dp[i][2] = min(dp[i][2], min(dp[i][1], dp[i][0]) + 1)

        return min(dp[t-1][0], dp[t-1][1], dp[t-1][2])

test = Solution()
obs = [0,2,1,0,3,0] # 2
# obs = [0,1,2,3,0] # 2
# obs = [0,3,3,0,3,2,2,0,0,3,0]
# obs = [0,2,2,1,0,3,0,3,0,1,0] # 1
# obs = [0, 2, 0]
res = test.minSideJumps(obs)
print(res)