from typing import List


class Solution:
    def stoneGame(self, piles: List[int]):
        if not piles:
            return False
        n = len(piles)
        # 定义二位数组的时候，注意不要用[base]*n，如果base改变，则n个base都会变
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i][0] = piles[i]
                
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                # choose left (after choose, change turn)
                left = piles[i] + dp[i+1][j][1]
                # choose right
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:   
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
           
        if dp[0][n-1][0] > dp[0][n-1][1]:
            return True
        return False
    
    def stoneGame_2(self, piles: List[int]) -> bool:
        even = sum([p for i, p in enumerate(piles) if i%2 == 0])
        odd = sum([p for i, p in enumerate(piles) if i%2 != 0])
        return even > odd



test = Solution()
piles = [3, 7, 2, 3]
# res = test.stoneGame(piles)
res = test.stoneGame_2(piles)
print(res)
                
                