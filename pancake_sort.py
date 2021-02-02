from typing import List


class Solution:
    """
    Solution 1: recursive. For n cakes, find the max pancake, and flip it to the bottom; process n-1 then.
    Solution 2: How to get the best solution
    """
    def pancakeSort(self, arr: List[int]) -> List[int]:

        res = []
        def helper(arr, n):
            nonlocal res
            if n == 1:
                return
            maxcake = 0
            maxcakeindex = 0
            for i in range(n):
                cake = arr[i]
                if cake > maxcake:
                    maxcake = cake
                    maxcakeindex = i
            arr[0:maxcakeindex+1] = arr[0:maxcakeindex+1][::-1]
            res.append(maxcakeindex+1)
            arr[:n] = arr[:n][::-1]
            res.append(n)
            
            helper(arr, n-1)
        
        helper(arr, len(arr))
        return res

test = Solution()
arr = [3,2,4,1]
res = test.pancakeSort(arr)
print(res)
