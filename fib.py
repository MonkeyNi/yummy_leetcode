class Solution:
    def fib(self, N: int) -> int:
        dp_0, dp_1 = 0, 1
        for _ in range(N):
            dp_0, dp_1 = dp_1, dp_0+dp_1
        return dp_0