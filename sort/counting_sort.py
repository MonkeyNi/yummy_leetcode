## 计数排序
## 空间换时间
## O(n+K)，稳定排序，外排序

def counting_sort(nums):
    if not nums:
        return nums
    n = len(nums)
    _min, _max = min(nums), max(nums)
    tmp_nums = [0]*(_max - _min + 1)
    # fill the extra space with frequency of elements
    for num in nums:
        tmp_nums[num - _min] += 1
    
    j = 0
    for i in range(n):
        while tmp_nums[j] == 0:
            j += 1
        nums[i] = j + _min
        tmp_nums[j] -= 1
    return nums

