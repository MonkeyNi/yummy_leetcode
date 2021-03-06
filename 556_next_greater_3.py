class Solution:
    def nextGreaterElement(self, n: int):
        ln = list(str(n))
        # find monotonic increasing substring (子串) from end
        j = len(ln) - 1
        while j >= 1 and ln[j] <= ln[j-1]:
            j -= 1
        if j == 0:
            return -1

        if j == len(ln) - 1:
            ln[-2], ln[-1] = ln[-1], ln[-2]
        else:
            # find the smallest element in increasing substring to replace ln[j]
            for i, ele in enumerate(ln[j:], start=j):
                if ele <= ln[j-1]:
                    i -= 1
                    break
            # replace
            ln[j-1], ln[i] = ln[i], ln[j-1]
            # reverse the increasing substring
            ln[j:] = ln[j:][::-1]
        
        res = int(''.join(ln))
        return res if res < (1<<31) else -1


test = Solution()
n = 2147483647
res = test.nextGreaterElement(n)
print(res)        
        
        
        