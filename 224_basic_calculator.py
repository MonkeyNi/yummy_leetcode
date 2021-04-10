class Solution:
    def calculate(self, s: str):

        def help(s):
            sign = '+'
            stack = []
            nums = 0
            while len(s) > 0:
            
            ## Why list enumerate will not work?
            # Becuase, we need to 'skip' parentheses part after calculate them as one number
            # If we use list enumerate, we will recalculate parentheses part when recusive is returned
            # 'for i, char in enumerate(s):'

                char = s.pop(0)
                if char.isdigit():
                    nums = nums*10 + int(char)
                if char == '(':
                    nums = help(s)

                # put nums to stack, depend on different situation
                # if goes to end of s, also need to add nums to stack
                if (char != ' ' and not char.isdigit()) or len(s) == 0:
                    if sign == '+':
                        stack.append(nums)
                    elif sign == '-':
                        stack.append(-nums)
                    
                    # remember to update sign and num
                    sign = char
                    nums = 0

                if char == ')':
                    break
            return sum(stack)
        
        return help(list(s))



test = Solution()
# s = "1 + 1"
s = "(1+(4+5+2)-3)+(6+8)"
res = test.calculate(s)
print(res)