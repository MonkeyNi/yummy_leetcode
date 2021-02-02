from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return []
        i, res = 0, []
        needs = Counter(p)
        missing = len(p)
        for j, c in enumerate(s, 1):
            missing -= needs[c]>0
            needs[c] -= 1
            if not missing:
                while i < j and needs[s[i]] < 0:
                    needs[s[i]] += 1
                    i += 1
                if j-i == len(p):
                    res.append(i)
        return res

test = Solution()
s, p = "cbaebabacd", "abc"
res = test.findAnagrams(s, p)
print(res)
