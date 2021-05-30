from collections import Counter


class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        pre = self.countAndSay(n-1)
        res = []
        freq = 1
        i = 1
        # consider end of string, we need add the freq
        while i <= len(pre):
            if i < len(pre) and pre[i] == pre[i-1]:
                freq += 1
            else:  # new char
                res.extend([str(freq), pre[i-1]])
                freq = 1
            i += 1
        return ''.join(res)


test = Solution()
n = 4
res = test.countAndSay(n)
print(res)