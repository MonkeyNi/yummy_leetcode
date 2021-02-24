# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode, build_tree


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        
        def help(root):
            nonlocal res
            if not root:
                return 1, 0, None, None
            ls, l, ll, lr = help(root.left)
            rs, r, rl, rr = help(root.right)
            
            if ((ls == 2 and lr < root.val) or ls == 1) and ((rs == 2 and rl > root.val) or rs == 1):
                size = root.val + l + r
                res = max(res, size)
                return 2, size, (ll if not ll is None else root.val), (rr if not rr is None else root.val)
            return 0, None, None, None
        
        help(root)
        return res
        
        
        
nums = [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
# nums = [1,None,10,-5,20]
# nums = [10, -5, 20]
root = build_tree(nums)

test = Solution()
res = test.maxSumBST(root)
print(res)