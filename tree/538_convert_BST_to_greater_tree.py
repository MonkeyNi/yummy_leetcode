from treeNode import TreeNode, build_tree


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        greater = 0
        
        def inorder(root):
            nonlocal greater
            
            if not root:
                return TreeNode(val=0)
            if root.right:
                root.right.val = inorder(root.right).val
            # right, root, left: decreasing order
            root.val += greater
            greater = root.val
            
            if root.left:
                root.left.val = inorder(root.left).val
            return root
        
        inorder(root)
        return root
        
        
nums = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
nums = [4,2,5,1,3,None,None]
nums = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = build_tree(nums)

test = Solution()
res = test.convertBST(root)
print(res)