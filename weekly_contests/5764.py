import math


class Solution:
    """
    Typical binary search problem.
    """
    def minSpeedOnTime(self, dist, hour):
        times = lambda s: sum(math.ceil(d / s) for d in dist[:-1])
        is_ontime = lambda s: times(s) + dist[-1] / s <= hour
        low, high = 1, 10**10
        while low < high:
            mid = low + (high - low) // 2
            if is_ontime(mid):
                high = mid
            else:
                low = mid + 1
        return low if is_ontime(low) else -1


test = Solution()
dist = [1, 3, 2]
hour = 2.7
res = test.minSpeedOnTime(dist, hour)
print(res)