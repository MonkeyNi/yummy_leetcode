# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        memo = {}
        
        def help(root):
            if root in memo:
                return memo[root]
            if root:
                rob_root = root.val + (
                    help(root.left.left)+help(root.left.right) if root.left else 0
                    ) + (
                        help(root.right.right)+help(root.right.left) if root.right else 0
                        )
                rob_no_root = help(root.left) + help(root.right)
                memo[root] = max(rob_root, rob_no_root)
                return memo[root]
            return 0
        
        help(root)
        return memo[root]
        
        