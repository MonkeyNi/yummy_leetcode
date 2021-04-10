from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        res = []

        def help(arr, n):
            if n == 0:
                return
            max_arr = max(arr[:n])
            ind_max = arr.index(max_arr)
            arr[:ind_max+1] = arr[:ind_max+1][::-1]
            res.append(ind_max+1)
            arr[:n] = arr[:n][::-1]
            res.append(n)
            help(arr, n-1)
        
        help(arr, len(arr))
        return res


test = Solution()
arr = [3,2,4,1]
res = test.pancakeSort(arr)
print(res)
