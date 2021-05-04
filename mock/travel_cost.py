class Solution:
    def twoCitySchedCost(self, costs):
        costs = sorted(costs, key=lambda x:x[0]-x[1])
        res = 0
        n = len(costs) // 2
        for i in range(n):
            res += (costs[i][0] + costs[i+n][1])
        return res

test = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
res = test.twoCitySchedCost(costs)
print(res)