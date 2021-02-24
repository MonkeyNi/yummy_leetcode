class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def build_tree(nums):
    ind_nums = nums.copy()
    
    def help(arrs):
        if not arrs:
            return None
        if arrs[0]:
            root = TreeNode(arrs[0])
        elif not arrs[0]:
            root = TreeNode(val=0)
        ind = ind_nums.index(arrs[0])
        root.left = help(arrs[ind+1:])
        root.right = help(arrs[ind+2:])
        return root
    
    return help(nums)