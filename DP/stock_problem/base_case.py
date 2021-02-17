"""
状态： 第几天 (i) / 可交易次数 (k) / 持有 (1) or未持有 (0)
选择： 交易（买卖）/ rest
"""


## Funtion
# ith天没有持有，那么前一天有两种情况，
#   1. 没有持有
#   2. 持有而且卖掉了
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + price[i])

# ith持有，前一天也有两种情况
#   1. 前一天持有而且没有交易
#   2. 前一天买入 (买入的情况下减去当前价格，减少一次交易次数)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price[i])


## Base case
# i start from 0, if i==-1, dp=0
dp[-1][k][0] = 0
dp[-1][k][1] = float('-inf') # cannot hold without trade
# k=0, dp=0
dp[i][0][0] = 0
dp[i][0][1] = float('-inf') # cannot hodl without trade


## Case 1, k = 1 (121)
# 这种情况下就可以忽略k的影响
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - price[i]) = max(dp[i-1][1], -price[i]) # since dp[i][0][0] = 0
dp[-1][0] = 0
dp[-1][1] = float('-inf')   


## Case 2, k = inf (122)
# 这种情况下也可以忽略k的影响
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - price[i])
dp[-1][0] = 0
dp[-1][1] = float('-inf')  


## Case 3, k = 2 (123)
## Case 3.1 k = integer (188)
##  考虑到内存问题，k <= len(prices)//2
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + price[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price[i])
dp[-1][k][0] = 0
dp[-1][k][1] = float('-inf') # cannot hold without trade
dp[i][0][0] = 0
dp[i][0][1] = float('-inf') # cannot hodl without trade


## Case 4, cooldown (k=inf) (309)
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - price[i])  # cooldown 1 day, i-2 instead of i-1
dp[-1][0] = 0
dp[-1][1] = float('-inf')


## Case 5, with transaction fee (k=inf) (714)
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - price[i] - fee)
dp[-1][0] = 0
dp[-1][1] = float('-inf')  
