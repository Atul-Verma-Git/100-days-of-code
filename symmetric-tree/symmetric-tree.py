# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if t1 == None and t2 == None:
                return True
            if (t1 == None and t2 != None) or (t2 == None and t1 != None) or (t1.val != t2.val) :
                return False
            else:
                return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
            

        if root == None:
            return True
        return isMirror(root.left,root.right)