import collections
from typing import List


# BFS 

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            cnt = 0
            for c in s:
                cnt += (c=='(')-(c==')')
                if cnt < 0:
                    return False
            return cnt == 0
        
        level = {s}
        while True:
            valid = list(filter(isvalid, level))
            if valid:  # since we just remove minimum
                return valid
            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}


test = Solution()
s = "()())()"
ans = test.removeInvalidParentheses(s)
print(f'All possible results: {ans}')        