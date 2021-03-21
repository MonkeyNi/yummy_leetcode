from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str):
        needs = Counter(s1)
        missing = len(s1)

        start = end = i = 0
        for j, ele in enumerate(s2, start=1):
            missing -= needs[ele] > 0
            needs[ele] -= 1
            if not missing:
                while i < j and needs[s2[i]] < 0:
                    needs[s2[i]] += 1
                    i += 1
                if not end or j-i < end-start:
                    start, end = i, j
        return (end-start) == len(s1)


test = Solution()
s1 = "ab"
s2 = "eidbaooo"
s1= "ab"
s2 = "eidboaoo"
res = test.checkInclusion(s1, s2)
print(res)
                    
