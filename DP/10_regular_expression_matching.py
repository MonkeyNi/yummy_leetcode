class Solution:
    """
    这题的难点在于'*'可以匹配0个或者n个，其实就是一个选择问题。
    这样的情况下，我们就需要考虑p[j+1]是否是‘*’。
    是‘*’： 0次匹配或者多次匹配
    不是‘*’：正常处理
    """
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def help(s, i, p, j):
            # base case
            if j == len(p):
                return i == len(s)
            if i == len(s):
                if (len(p)-j)%2 == 1:
                    return False
                else:
                    for t in range(j+1, len(p), 2):
                        if p[t] != '*':
                            return False
                    return True
            
            if (s, i, p, j) in memo:
                return memo[(s, i, p, j)]
            
            # state function
            if s[i] == p[j] or p[j] == '.':
                if j < len(p) - 1 and p[j+1] == '*':
                    memo[(s, i, p, j)] = help(s, i, p, j+2) or help(s, i+1, p, j)
                else:
                    memo[(s, i, p, j)] = help(s, i+1, p, j+1)
            else:
                if j < len(p) - 1 and p[j+1] == '*':
                    memo[(s, i, p, j)] = help(s, i, p, j+2)
                else:
                    memo[(s, i, p, j)] = False
            return memo[(s, i, p, j)]
        
        return help(s, 0, p, 0)
    
test = Solution()
s = "aa"
p = "a"
s = "aa"
p = "a*"
s = "ab"
p = ".*"
s = "aab"
p = "c*a*b"
s = "mississippi"
p = "mis*is*p*."
res = test.isMatch(s, p)
print(res)
        