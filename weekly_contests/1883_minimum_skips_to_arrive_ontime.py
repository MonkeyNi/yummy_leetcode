from math import ceil


class Solution:
    """
    All info: ith road, number of skip, time will cost, (speed?)
    dp[i][j]: arrive at road i with j skip will cost this time in minimum.
    Then dp[i][j] = min(skip ith, not skip ith), which is min(
        dp[i-1][j-1] + dist[i]/speed, # skip ith road rest
        ceil(dp[i-1][j] + dist[i]/speed) # do not skip ith road rest
    )
    """
    def minSkips(self, dist, speed, hoursBefore):
        esp = 1e-9
        n = len(dist)
        dp = [[10**10 for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0] = 0
        for i, d in enumerate(dist, 1):
            ### Note
            # it is not dp[i-1][0]+ceil(d/speed), 
            # since we do not need to rest at the last road
            dp[i][0] = ceil(dp[i-1][0] + d/speed-esp) 
            for j in range(1, i+1):
                dp[i][j] = min(
                    ceil(dp[i-1][j] + d/speed-esp),
                    dp[i-1][j-1] + d/speed
                )
        for j, t in enumerate(dp[-1]):
            if t <= hoursBefore:
                return j
        return -1

test = Solution()
dist = [1, 3, 2]
speed = 4
hourBefore = 2

res = test.minSkips(dist, speed, hourBefore)
print(res)
        