from bisect import bisect_left as bl
from typing import List

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]):
        """
        Find the max diff difference if we change one element to another one
        """
        if not nums1 and not nums2:
            return 0
        
        sort_n1 = sorted(nums1)
        
        res = 0
        max_diff = 0
        for a, b in zip(nums1, nums2):
            ori_diff = abs(a - b)
            res += ori_diff
            
            ind = bl(sort_n1, b)
            if ind == 0:
                min_diff = abs(b - sort_n1[0])
            elif ind == len(nums1):
                min_diff = abs(b - sort_n1[-1])
            else:
                min_diff = min(abs(b - sort_n1[ind]), abs(b - sort_n1[ind-1]))
            
            max_diff = max((ori_diff - min_diff), max_diff)
        
        return (res - max_diff) % (pow(10, 9) + 7)