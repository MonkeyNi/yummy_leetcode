from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        MAX = float('inf')
        # dp table to record status
        dp = [0] + [MAX]*amount
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return [dp[-1], -1][dp[-1]==MAX]
    
    def coinChange_2(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if (i-c)>=0 else MAX for c in coins]) + 1
        return [dp[-1], -1][dp[-1]==MAX]

    # 20210207
    def coinChange3(self, coins: List[int], amount: int):
        if not amount:
            return 0
        # Do not forget base case
        dp_table = [0] + [amount+1]*amount

        for i in range(1, len(dp_table)):
            for coin in coins:
                if i - coin < 0:
                    continue
                # follow status function
                dp_table[i] = min(dp_table[i], dp_table[i-coin]+1)
        return -1 if (dp_table[amount]==amount+1) else dp_table[amount]
    
    # 20210715
    def coinChange4(self, coins: List[int], amount: int):
        if not amount: return 0
        # remove duplicate sub-questions
        memo = {0:0}
        def dp(n):
            if n in memo: return memo[n]
            # base cases
            if n == 0: return 0
            if n < 0: return -1
            # initialize res
            res = float('inf')
            for c in coins:
                left = dp(n-c)
                if left < 0: continue
                res = min(res, 1+left)
            memo[n] = res if res != float('inf') else -1
            return memo[n]
        dp(amount)
        return memo[amount]

test = Solution()
coins = [1]
amount = 0
res = test.coinChange4(coins, amount)
print(res)