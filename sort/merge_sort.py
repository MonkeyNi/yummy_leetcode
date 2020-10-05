## 分合的思想，把数组分开排序，然后再合并
## 稳定排序，外排序（占用额外内存），时间复杂度O(nlogn)

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    return merge(left, right)


def merge(left, right):
    res = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        
    res += left[i:]
    res += right[j:]
    return res
