from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l <= r:
            tmp = numbers[l] + numbers[r]
            if tmp == target:
                return [l+1, r+1]
            elif tmp > target:
                r -= 1
            elif tmp < target:
                l += 1
        else:
            return None

test = Solution()
nums, t = [2,7,11,15], 9
res = test.twoSum(nums, t)
print(res)