from typing import List


class Solution:
    def trap_viloence(self, height: List[int]) -> int:
        """
        Viloent Solution: TC: O(N^2); SC: O(1)
        """
        if not height:
            return 0
        
        res = 0
        for i in range(1, len(height)):
            r_max, l_max = 0, 0
            # right max
            for j in range(i):
                r_max = max(r_max, height[j])
            # left max
            for j in range(i+1, len(height)):
                l_max = max(l_max, height[j])
            
            res += max((min(r_max, l_max) - height[i]), 0) # cannot be negative
        return res
    
    def trap_memo(self, height: List[int]) -> int:
        """
        Memo: TC: O(N), SC: O(N)
        """
        if not height:
            return 0
        
        res = 0
        r_max = [0 for _ in range(len(height))]
        tmp_r_max = height[0]
        for i in range(1, len(height)):
            r_max[i] = tmp_r_max
            tmp_r_max = max(tmp_r_max, height[i])
        
        l_max = [0 for _ in range(len(height))]   
        tmp_l_max = height[-1]
        for i in range(len(height)-1, -1, -1):
            l_max[i] = tmp_l_max
            tmp_l_max = max(tmp_l_max, height[i])
        
        for i in range(1, len(height)-1):
            res += max(0, (min(r_max[i], l_max[i]) - height[i]))
        return res
    
    def trap_double_pointers(self, height: List[int]) -> int:
        """
        Double pointers: TC: O(N); SC: O(1)
        """
        if not height:
            return 0
        
        res = 0
        right = 0
        left = len(height) - 1
        r_max, l_max = 0, 0
        while right <= left:
            r_max = max(r_max, height[right])
            l_max = max(l_max, height[left])
            
            if r_max < l_max:
                res += max(0, (r_max - height[right]))
                right += 1
            else:
                res += max(0, (l_max - height[left]))
                left -= 1         
        return res
        
    
    
test = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
res = test.trap_double_pointers(height)
print(res)