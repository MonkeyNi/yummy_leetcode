class Solution:
    def splitString(self, s: str) -> bool:
        for i, n in enumerate(s):
            cur = int(s[:i+1])
            start = i + 1
            end = start + 1
            while end <= len(s):
                # if cur number is 1, end all left must be 0s
                if cur == 1 and end < len(s) and int(s[end:]) == 0:
                        return True
                else:
                    break
                next_n = int(s[start:end])
                if next_n + 1 == cur:
                    cur = next_n
                    start = end
                    end = start + 1
                    if start == len(s):
                        return True
                elif next_n + 1 < cur:
                    end += 1
                else:
                    break
        return False
    
    def backtrace(self, s):
        def help(s, x):
            # initial situation
            if x == None:
                for i in range(1, len(s)):
                    if help(s[i:], int(s[:i])):
                        return True
                return False
            else:
                if s == '' or int(s) == x - 1:
                    return True
                else:
                    for i in range(1, len(s)):
                        if int(s[:i]) + 1 == x:
                            return help(s[i:], x-1)
            return False
        return help(s, None)
        

test = Solution()
s = "050043"
s = "1234"
s = "9080701"
s = "10009998"
# s = "200100"
# s = "1000"
# s = "1110987605"
res = test.splitString(s)
res = test.backtrace(s)
print(res)