class Solution:
    """
    Check 84: largest Rec in histogram
    
    monotone stack!!! 
    Key point: for each element, calculate the maxmum value when the element is the samllest one;
        1. For each element, we need to find the right and left border (next smaller element);
        2. calculate sum between i, j (presum)
    """
    def maxSumMinProduct(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        right, left = [0]*n, [n-1]*n
        stack = []
        # find the next smaller one in the left
        # using monotone increasing stack
        for i, ele in enumerate(nums):
            while stack and ele < nums[stack[-1]]:
                left[stack.pop(-1)] = i - 1
            stack.append(i)
        stack = []
        # find the next smaller one in the right
        for i in range(n-1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                right[stack.pop(-1)] = i + 1
            stack.append(i)
        
        presum = [0]*(n+1)
        for i, ele in enumerate(nums):
            presum[i+1] = presum[i] + nums[i]
            
        def getsum(i, j):
            # compute presum from i to j (include both i and j): presum[j] - presum[i-1]
            return presum[j+1] - presum[i]
        
        ans = 0
        for i, ele in enumerate(nums):
            # print(f'i: {i}, ele: {ele}, right: {right[i]}, left: {left[i]}')
            ans = max(ans, ele*(getsum(right[i], left[i])))
        return int(ans/(10**9+7))
        
    def maxSumMinProduct_2(self, nums):
        """
        Same process as max histogram
        """
        nums.append(float('-inf'))
        stack = [-1]
        n = len(nums)
        presum = [0]*(n+1)
        
        for i, ele in enumerate(nums):
            presum[i+1] = presum[i] + nums[i]
            
        ans = 0
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                h = stack.pop(-1)
                # we do not need the left and right border
                ans = max(ans, nums[h]*(presum[i]-presum[stack[-1]+1]))
            stack.append(i)
        return ans

test = Solution()
nums = [1,2,3,2] # 14
nums = [2,3,3,1,2] # 18
res = test.maxSumMinProduct_2(nums)
print(res)