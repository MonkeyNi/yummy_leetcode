## 通过选定锚点（通常可以选择为第一个element）
## 同时双向遍历数据，调整数据位置
## 当指针重叠时，更新锚点位置，再分别对锚点左右进行相同的操作

def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums
        pivot = left
        i = left
        j = right
        while i < j:
            if nums[i] < nums[pivot]:
                i += 1
            if nums[j] >= nums[pivot]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j] , nums[pivot]
        quick(left, j-1)
        quick(j+1, right)
        return nums

    return quick(0, n-1)