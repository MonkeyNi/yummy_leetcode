from typing import List


class Solution:
    """
    Releated problem: 556
    """
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        while j >= 1 and nums[j] <= nums[j-1]:
            j -= 1
        
        if j == 0:
            nums[:] = nums[::-1] # not nums = nums[::-1]
        else:
            for i, ele in enumerate(nums[j:], start=j):
                # find the first ele which is larger than nums[j-1] in nums[j:]
                if nums[i] <= nums[j-1]:
                    i -= 1
                    break
            
            # replace 
            nums[j-1], nums[i] = nums[i], nums[j-1]
            # change from maximum to minimum
            nums[j:] = nums[j:][::-1]

        return nums

test = Solution()
nums = [3, 2, 1]
res = test.nextPermutation(nums)
print(res)
