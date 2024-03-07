import time

class Solution:
    def search(self, nums, target):
        result = [-1, -1]
        if not len(nums):
            return result
        if len(nums) == 1:
            if nums[0] != target:
                return result
            else:
                return [0, 0]
        
        # get left border [left, right]
        left = 0
        right = len(nums) - 1
        ### NOTE: 如果不用左右闭区间, 很难写...
        while left <= right:
            mid = (left + right) // 2
            mn = nums[mid]
            if mn > target:
                right = mid - 1
            elif mn < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            result[0] = left
        else:
            return result
        
        # get right border [left, right]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mn = nums[mid]
            if mn > target:
                right = mid - 1
            elif mn < target:
                left = mid + 1
            else:
                left = mid + 1
        if nums[right] == target:
            result[1] = right
        else:
            return result
        
        return result
    

def test():
    bs = Solution()
    nums_list = [
        [1, 2, 2, 2, 2, 2, 3],  # [1, 5]
        [],                     # [-1, -1]
        [0],                    # [-1, -1]
        [2]                     # [0, 0]
    ]
    target = 2
    for nums in nums_list:
        print(bs.search(nums, target))
        

if __name__ == "__main__":
    test()
    
    