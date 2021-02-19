class Solution:
    """
    Substrings are consecutive subsequence.
    dp[i][j]: if s[i:j] is palindrome
    
    This problem is different from 'longest palindrome subsquence'
    """
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        dp = [[False for _ in range(len(s))] for _  in range(len(s))]
        # base case
        for i in range(len(s)):
            dp[i][i] = True
        
        res = 0
        start = 0
        max_res = 1
        for i in range(len(s)-1, -1, -1):
            for dest in range(1, len(s) - i):
                j = dest + i
                if dest == 1 and s[i] == s[j]:
                    dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and j-i+1 > max_res:
                    max_res = j - i + 1
                    start = i
        return s[start:start+max_res]
    
    
test = Solution()
s = "babad"
# s = "cbbd"
# s = "a"
s = "ac"
s = "aacabdkacaa"
res = test.longestPalindrome(s)
print(res)