from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        if not s or not p:
            return []

        res = []
        i = 0
        needs = Counter(p)
        missing = len(p)
        for j, ele in enumerate(s, start=1):
            missing -= needs[ele]>0
            needs[ele] -= 1
            if not missing:
                while i < j and needs[s[i]] < 0:
                    needs[s[i]] += 1
                    i += 1
                if j - i == len(p):
                    res.append(i)
        return res


test = Solution()
s = "cbaebabacd"
p = "abc"
res = test.findAnagrams(s, p)
print(res)