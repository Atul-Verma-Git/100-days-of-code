# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def remove(head, val):
            if head == None:
                return head
            elif head.val == val:
                head = head.next
                return remove(head, val)
            else:
                head.next = remove(head.next , val)
                return head
                
        
        return remove(head,val)
        
            
        