def move1(nums):
    # same question as 'move all zeros to the end.'
    # Move zeros, which also means that move non-0 to the other side
    # So, this question is actually move all non-0 to the end
    # Just traverse from the end, record current index and move non-0 to this index
    if len(nums) <= 1:
        return nums
    end = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if nums[i]:
            nums[i], nums[end] = nums[end], nums[i]
            end -= 1
    return nums

# nums = [1,2,3,0,0]
# nums = [2,0,5,0,2,3,4,50,2,0]
# nums = [0,0,0,0]
# nums = [0,0,0,1,2]
nums = [[], [1], [0], [1,2,3,0,0], [2,0,5,0,2,3,4,50,2,0], [0,0,0,0], [0,0,0,1,2], [0,0,1,2,0,0]]
for num in nums:
    print(move1(num))

        