import math


class Solution:
    """
    埃拉托斯特尼筛法- 维基百科，自由的百科全书
    以每个素数本身做为等差数列，去排除
    """
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        res = [True for _ in range(n)]
        for i in range(2, n):
            if i*i > n:
                break
            if res[i]:
                for j in range(i*i, n, i):
                    res[j] = False
        return sum(res) - 2


test = Solution()
n = 0
res = test.countPrimes(n)
print(res)