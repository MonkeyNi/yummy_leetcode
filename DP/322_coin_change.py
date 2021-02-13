from typing import List


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

    # 20210207
    def coinChange3(self, coins: List[int], amount: int):
        # Do not forget base case
        dp_table = [0] + [amount+1]*amount

        for i in range(1, len(dp_table)):
            for coin in coins:
                if i - coin < 0:
                    continue
                # follow status function
                dp_table[i] = min(dp_table[i], dp_table[i-coin]+1)
        return -1 if (dp_table[amount]==amount+1) else dp_table[amount]
        

test = Solution()
coins = [1, 2, 5]
amount = 11
res = test.coinChange3(coins, amount)
print(res)