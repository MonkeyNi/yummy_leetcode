# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        def help(root):
            nonlocal pre
            if not root:
                return True
            if not help(root.left):
                return False
            # use inorder traverse (Space complexity O(1))
            if root.val <= pre:
                return False
            pre = root.val
            
            return help(root.right)
        
        return help(root)
    
    def isValidBST_2(self, root: TreeNode) -> bool:
        
        def help(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            if root.val <= lower:
                return False
            if root.val >= upper:
                return False
            return help(root.left, lower=lower, upper=root.val) and help(root.right, lower=root.val, upper=upper)
        return help(root)