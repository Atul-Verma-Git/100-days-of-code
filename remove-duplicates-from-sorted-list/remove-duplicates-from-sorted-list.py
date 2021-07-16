# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def dup(head):
            if head == None:
                return head
            elif head.next == None:
                return head
            elif head.val == head.next.val:
                head.next = head.next.next
                head = dup(head)
                return head
            else:
                head.next = dup(head.next)
                return head
                
        return dup(head)
        