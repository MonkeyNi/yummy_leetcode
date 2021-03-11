class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []

        def dfs(nums, path):
            """
            dfs(selection list, current path)
            """
            # no more selection, add current path to result
            if not nums:
                res.append(path)
                return
            for i, ele in enumerate(nums):
                selection = nums[:i] + nums[i+1:]
                selected = nums[i]
                # since I did not 'directly add' selected to path, so I donot need to pop
                # Standard way:
                #   path.append(selected)
                #   backtrace()
                #   path.pop(selected)
                dfs(selection, path+[selected])
            return
        
        dfs(nums, [])
        return res