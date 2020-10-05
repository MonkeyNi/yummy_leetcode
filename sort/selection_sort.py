## 选择排序，最直接的排序方式
## Time complexity: O(n^2)

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[j] <= nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums