# Actually, KMP is much more slower than str.find()....


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Normal solution: Time complexity: O(MN)
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1
    
        # KMP solution: Time complexity: O(N)
        dp = self.KMP(needle)
        return self.search(haystack, needle, dp)
    
    def KMP(self, pat):
        M = len(pat)
        dp = [[0 for _ in range(256)] for _ in range(M)]
        dp[0][ord(pat[0])] = 1
        pre_pat = 0
        for j in range(1, M): # start from 1 instead of 0 (since base case is 0)
            for c in range(256):
                if ord(pat[j]) == c:
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[pre_pat][c]
            pre_pat = dp[pre_pat][ord(pat[j])]
        return dp
    
    def search(self, txt, pat, dp):
        M = len(pat)
        N = len(txt)
        j = 0
        for i in range(N):
            print(f' Pre j: {j}, {txt[i]}')
            j = dp[j][ord(txt[i])]
            print(j)
            if j == M:
                return i - M + 1
        return -1
    
    
test = Solution()
haystack = "mississippi"
needle = "issip"
# haystack = "hello"
# needle = "ll"
res = test.strStr(haystack, needle)
print(f'Result: {res}')
    