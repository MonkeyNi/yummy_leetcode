# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            # Root has zero or 1 child
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # root has more than 2 child, then replace root.val with the minimum val in the right subtree
            root.val = self.get_min(root.right)
            # after replace, delete the minimum
            root.right = self.deleteNode(root.right, root.val)
            
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

    def get_min(self, root):
        while root.left:
            root = root.left
        return root