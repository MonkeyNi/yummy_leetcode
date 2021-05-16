def subsetXORSum(nums):
    if not nums:
        return 0
    
    from itertools import combinations
    n = len(nums)
    res = 0
    for i in range(1, n+1):
        for com in combinations(nums, i):
            tmp = 0
            for ele in com:
                tmp ^= ele
            res += tmp
    return res

def minSwaps(s):
    if len(s) <= 1:
        return 0
    n = len(s)
    
    # check if original is ok
    flag = True
    for a, b in zip(s, s[1:]):
        if a == b:
            flag = False
            break
    if flag:
        return 0
    
    from collections import Counter
    
    sd = Counter(s)
    n1 = sd['1']
    n0 = sd['0']
    
    # diff over 1 mean impossible
    if abs(n1-n0) > 1:
        return -1
    
    st1 = list(s)
    st2 = list(s)
    if n1 > n0:
        # start with 1
        st1[0::2] = ['1']*n1
        st1[1::2] = ['0']*n0
        diff = sum([int(a)^int(b) for a, b in zip(st1, list(s))])
        return int(diff//2)
    elif n0 > n1:
        st2[0::2] = ['0']*n0
        st2[1::2] = ['1']*n1
        diff = sum([int(a)^int(b) for a, b in zip(st2, list(s))])
        return int(diff//2)
    else: # n1==n0
        # start '0'
        st1[0::2] = ['0']*n0
        st1[1::2] = ['1']*n1
        diff1 = sum([int(a)^int(b) for a, b in zip(st1, list(s))])
        # start '1'
        st2[0::2] = ['1']*n1
        st2[1::2] = ['0']*n0
        diff2 = sum([int(a)^int(b) for a, b in zip(st2, list(s))])
        return int(min(diff1, diff2)//2)

def q3():
    pass

def q4(n, k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, min(n, k)+1):
            dp[i][j] = dp[i-1][j]*(i-1) + dp[i-1][j-1]
            dp[i][j] %= (10**9+7)
    return int(dp[n][k]%(10**9+7))


nums = [1, 3]
nums = [3,4,5,6,7,8]
print(subsetXORSum(nums))

s = '111000'
s = "1110"
s = "010"
print(minSwaps(s))
print(q3())
n = 20
k = 11
print(q4(n, k))