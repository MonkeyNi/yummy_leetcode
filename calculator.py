def calculate(s: str) -> int:
        
        def helper(s):
            num = 0
            sign = '+'
            stack = []
            while len(s) > 0:
                char = s.pop(0)
                if char.isdigit():
                    num = num*10 + int(char)
                
                if char == '(':
                    num = self.calculate(s)
                
                if (not char.isdigit() and char != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    num = 0
                    sign = char
                if char == ')':
                    break
            return sum(stack)
                
        return helper(list(s))

s = '"(1+(4+5+2)-3)+(6+8)"'
calculate(s)