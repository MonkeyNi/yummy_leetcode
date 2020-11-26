class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        # dp table to record status
        dp = [0] + [MAX]*amount
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return [dp[-1], -1][dp[-1]==MAX]
    
    def coinChange_2(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if (i-c)>=0 else MAX for c in coins]) + 1
        return [dp[-1], -1][dp[-1]==MAX]