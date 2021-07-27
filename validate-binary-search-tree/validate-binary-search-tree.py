# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        s = []
        def inorder(root):
            if root == None:
                pass
            else:
                inorder(root.left)
                s.append(root.val)
                inorder(root.right)
        inorder(root)
        
        for x in range(1,len(s)):
            if s[x-1] >= s[x]:
                return False
        return True
            
        