## Ref: https://www.chainnews.com/articles/378340495318.htm
## 希尔排序是插入排序的升级版，对目标数据进行预调整，目的是为了减少排序的工作量
## Note: 因为考虑到某些元素可能已经有序, 可以考虑最极端的例子，降序数组变成升序数组
## Note: 某些时候可能比插入排序更差
## 增量序列 [1,2,3,4] / [1,3,5,7] / or better 
## 非稳定，內排序

def hill_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i-gap > 0 and nums[i-gap] >= nums[i]:
                nums[i-gap], nums[i] = nums[i], nums[i-gap]
                i -= gap
        gap //= 2
    return nums