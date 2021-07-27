# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        output = [[]]
        q = [[]]
        count = 0
        q[0].append(root)
        while q[count] != []:
            q.append([])
            count += 1
            while q[count-1] != []:
                temp = q[count-1].pop(0)
                if temp.left != None:
                    q[count].append(temp.left)
                if temp.right != None:
                    q[count].append(temp.right)
                output[count-1].append(temp.val)
            if q[count] != []:
                output.append([])
        return output
            
        
        
        
        