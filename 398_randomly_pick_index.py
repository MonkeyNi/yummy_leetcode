from tpying import List


class Solution:
    """
    Set pick ith element probability as 1/i, and not replace ith element in after probability is (1-1/i).
    Then for n elements, it has 1/n probability to pick an element
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        nums = self.nums
        res = 0
        ind = 0
        for i, ele in enumerate(nums):
            if ele == target:
                if random.randint(0, ind) == 0:
                    res = i
                ind += 1 # noted
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)