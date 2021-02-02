from collections import  Counter 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        i = 0
        res = 0
        needs = Counter()
        for j, c in enumerate(s, 1):
            needs[c] += 1
            while needs[c] > 1:
                needs[s[i]] -= 1
                i += 1
            res = max(res, j-i)
        return res
    
test = Solution()
s = "bbb"
res = test.lengthOfLongestSubstring(s)
print(res)

