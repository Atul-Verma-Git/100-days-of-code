# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output= temp = ListNode(0)
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        while l1 or l2:
            if l1:
                first = l1.val
            else:
                temp.val = l2.val
                temp.next = l2.next
                return output
            if l2:
                sec = l2.val
            else:
                temp.val = l1.val
                temp.next = l1.next
                return output
            if sec > first:  
                temp.val = first
                l1 = l1.next
            else:
                temp.val = sec
                l2 = l2.next
            tn = ListNode(0)
            temp.next = tn
            temp = temp.next
        return output
                
            
        
            
            
            
        
                