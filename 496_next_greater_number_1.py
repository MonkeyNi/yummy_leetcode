from typing import List


class Solution:
    """
    Monotonic stack.
    For each element, it has been push (and pop) at most one time. O(n)
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        if not nums1 or not nums2:
            return []
        res = {a:-1 for a in nums2}
        stack = []
        for i, ele in enumerate(nums2):
            #  检查当前元素是前面哪儿些元素的next greater element
            while stack and ele > nums2[stack[-1]]:
                res[nums2[stack.pop()]] = i
            stack.append(i)
        return [res[a] for a in nums1]


test = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = test.nextGreaterElement(nums1, nums2)
print(res)