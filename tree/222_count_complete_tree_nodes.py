# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        
        if left_depth == right_depth:
            # left sub tree if a perfect binary tree and right sub tree is a complete binary tree
            # since we need to add root, so it is math.pow(2, depth) - 1 + 1 + the_other_sub_tree
            return int(math.pow(2, left_depth) + self.countNodes(root.right))
        else:
            # the opposite situation
            return int(math.pow(2, right_depth) + self.countNodes(root.left))
        
    def get_depth(self, root):
        if not root:
            return 0
        return 1 + self.get_depth(root.left)