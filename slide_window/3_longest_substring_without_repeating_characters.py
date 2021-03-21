from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        
        needs = Counter()
        j = 0
        res = 0
        for i, ele in enumerate(s, start=1):
            needs[ele] += 1
            while needs[ele] > 1 and j < i:
                needs[s[j]] -= 1
                j += 1
            res = max(res, i-j)
        return res


test = Solution()
s = "abcabcbb"
s = "bbbbb"
res = test.lengthOfLongestSubstring(s)
print(res)
