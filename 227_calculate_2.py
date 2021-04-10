class Solution:
    def calculate(self, s: str):
        num = 0
        sign = '+'
        stack = []

        for i, char in enumerate(s):
            if char.isdigit():
                num = num*10 + int(char)
            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/num)
                num = 0
                sign = char
        return sum(stack)

test = Solution()
s = "14-3/2"
res = test.calculate(s)
print(res)