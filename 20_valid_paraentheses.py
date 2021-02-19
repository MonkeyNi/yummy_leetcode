class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        paeses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i, ele in enumerate(s):
            if ele in paeses:
                left.append(ele)
            elif left and ele == paeses[left[-1]]:
                left.pop()
            else:
                return False
        return not left 
    
    
test = Solution()
s = "()"
s = "()[]{}"
s = "([)]"
s = "{[]}"
res = test.isValid(s)
print(res)