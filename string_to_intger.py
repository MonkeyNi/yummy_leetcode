class Solution:
    def myAtoi(self, s: str) -> int:
        sign = '+'
        res = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                break
        ss = s[i:]
        if len(ss) == 0:
            return 0
        if not ss[0].isdigit() and ss[0] != '+' and ss[0] != '-':
            return 0
        else:
            i = 0
            if not ss[0].isdigit():
                sign = ss[0]
                i = 1

            while i < len(ss):
                if ss[i].isdigit():
                    res.append(ss[i])
                    i += 1
                else:
                    break
            if not res:
                return 0
            sign = 1 if sign == '+' else -1
            return max(min(int(''.join(res))*sign, 2**31-1), -2**31)

test = Solution()
s = '+-12'
res = test.myAtoi(s)
print(res)