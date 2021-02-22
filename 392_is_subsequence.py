from collections import defaultdict
import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
    
    def isSubsequence_2(self, s: str, t: str) -> bool:
        """
        Binary search
        """
        dir = defaultdict(list)
        for i, ele in enumerate(t):
            dir[ele].append(i)
        
        res = -1
        for ele in s:
            if not ele in dir:
                return False
            # when there are same characters in s, insert in the right
            ind = bisect.bisect_right(dir[ele], res)
            # exceed the previous max index
            if ind == len(dir[ele]):
                return False
            res = dir[ele][ind]
        if res >= len(t):
            return False
        return True
            
            
             
    

test = Solution()
s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s = "acb"
# t = "ahbgdc"
# s = "aaaaaa"
# t = "bbaaaa"
res = test.isSubsequence_2(s, t)
print(res) 
