## 遍历数组，逐步把剩余的元素插入到已经排好序的部分中
## 稳定排序，内排序，时间复杂度：O(n^2)

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        while i > 0 and nums[i-1] >= nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1
    return nums