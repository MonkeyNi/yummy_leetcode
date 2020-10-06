## 计数排序的进阶版本，通过控制bucket size，减少额外空间的使用
## 稳定排序，外排序，时间复杂度O(n + k)，k为桶的个数。

def bucket_sort(nums, bucket_size):
    if not nums:
        return nums
    _min, _max = min(nums), max(nums)
    bucket_num = (_max-_min)//bucket_size + 1
    tmp_buckets = [[] for _ in range(bucket_num)]
    for num in nums:
        tmp_buckets[(num-_min)//bucket_size].append(num)
    res = []
    for bucket in tmp_buckets:
        if not bucket:
            continue
        if bucket_size == 1:
            res.extend(bucket)
        else:
            if bucket_num == 1:
                bucket_size -= 1
            res.extend(bucket_sort(bucket, bucket_size))
    return res

