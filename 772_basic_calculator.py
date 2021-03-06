"""
实现计算器，我们需要实现及处理一下几种情况：
1. 加减乘除
2. remove 空格
3. 运算的优先级
4. 括号问题
5. 因为是从字符串读入，所以需要考虑字符转整型的问题
6. 异常处理： 整型溢出（pyhton3中不会发生），除数是0
"""
class Solution:
    def calculate(self, s: str) -> int:

        def helper(s):
            stack = []
            sign = '+'
            nums = 0
            while len(s) > 0:
                char = s.pop(0)
                if char.isdigit():
                    nums = 10*nums + int(char)
                if char == '(':
                    nums = helper(s)
                if (char != ' ' and not char.isdigit()) or len(s) == 0:
                    if sign == '+':
                        stack.append(nums)
                    elif sign == '-':
                        stack.append(-nums)
                    elif sign == '*':
                        stack[-1] = stack[-1]*nums
                    elif sign == '/':
                        stack[-1] = int(stack[-1]/float(nums))
                    nums = 0
                    sign = char
                if char == ')':
                    break
            return sum(stack)
        return helper(list(s)) # convert string to list first


test = Solution()
s = " 3/2 "
res = test.calculate(s)
print(res)