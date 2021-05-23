import math

class Solution:
    def minSpeedOnTime(self, dist, hour):
        times = lambda s: sum(math.ceil(d / s) for d in dist[:-1])
        is_ontime = lambda s: times(s) + dist[-1] / s <= hour
        base = times(1)
        low, high = 1, base + math.ceil(dist[-1] / (hour - base))
        # while low + 1 < high:
        while low < high:
            mid = low + (high - low) // 2
            print(mid)
            if is_ontime(mid):
                high = mid
            else:
                low = mid + 1
        return high if is_ontime(high) else -1

test = Solution()
dist = [1, 3, 2]
hour = 6
res = test.minSpeedOnTime(dist, hour)
print(res)