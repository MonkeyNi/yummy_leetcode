class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        
        res = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i])*int(num2[j])
                
                p, q = i+j, i+j+1
                mul += res[q]
                res[q] = mul % 10
                res[p] = res[p] + mul // 10
        
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        res_str = "".join(list(map(str, res[i:])))
        return '0' if not res[i:] else res_str
    

test = Solution()
num1 = "2"
num2 = "3"
num1 = "123"
num2 = "456"
res = test.multiply(num1, num2)
print(res)