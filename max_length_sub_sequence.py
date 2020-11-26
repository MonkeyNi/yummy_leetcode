import bisect

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

def lengthOfLIS_binary(nums):
    """Use binary search find the left split index, and then keep monotone

    Args:
        nums ([type]): [description]

    Returns:
        [type]: [description]
    """
    ans = []
    for num in nums:
        ind = bisect.bisect_left(ans, num)
        if ind == len(ans):  # mean monotone
            ans.append(num)
        else:
            ans[ind] = num
        print(ans)
    return len(ans)

test = [10,9,2,5,3,7,101,18]
res = lengthOfLIS(test)
print(res)
print(lengthOfLIS_binary(test))