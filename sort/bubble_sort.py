## 冒泡排序，通过两两选择，把大数沉底
## Time complexity: O(n^2)， 稳定排序， 內排序

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(1, n-i):
            if nums[j] <= nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums