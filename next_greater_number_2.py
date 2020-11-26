def nextGreaterElements(nums):
    res = [0]*len(nums)
    stack = []
    for i in range(len(nums)*2):
        circle_i = i % len(nums)
        print(circle_i)
        while stack and nums[circle_i] > nums[stack[-1]]:
            res[stack.pop()] = nums[circle_i]
        stack.append(circle_i)
    return res

res = nextGreaterElements([3,5,2,2,5,5,4,1])
print(res)
