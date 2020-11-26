def lengthOfLIS(nums):
    if not nums:
        return []
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    return max(dp)

test = [10,9,2,5,3,7,101,18]
res = lengthOfLIS(test)
print(res)