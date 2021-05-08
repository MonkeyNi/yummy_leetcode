from typing import List


class Solution:
    """
    4个key，A, ctrl + A, ctrl + C, ctrl + V，可以操作N次，怎么样可以得到最多的A。
    考虑到CA，CC，CV至少占用两次操作，所以在N较小的时候，全部输入A；N比较大的情况下，
    可以用AAAA， CA，CC，CV，CV，CV。。。。CA，CC，CV，CV。。。所以我们只需要记录CV的起点（j）
    就可以了。
    
    20210508
    Key point: end operation is either 'A' or 'Ctrl-V'
    """
    def keyboard(self, n):
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(2, i):
                dp[i] = max(
                    dp[i], dp[j-2]*(i-j+1)
                )
        return dp[-1]

test = Solution()
n = 7
res = test.keyboard(n)
print(res)