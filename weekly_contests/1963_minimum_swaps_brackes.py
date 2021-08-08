class Solution:
    def minSwaps(self, s: str):
        """
        Check how many illegal ] before [, then we need how many steps
        """
        right = 0  # how many [ 
        ans = 0
        for b in s:
            right = right + 1 if b == '[' else right - 1
            if right < 0:
                ans += 1
                right = 1  # since we have change ] to [, then right should be 1 instead of 0
        return ans