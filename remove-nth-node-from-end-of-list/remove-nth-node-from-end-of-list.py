# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        temp = head
        curr = head
        while n > 0:
            temp = temp.next
            n -= 1
        if temp == None:
            return head.next
        while temp.next:
            curr = curr.next
            temp = temp.next
        curr.next = curr.next.next
        return head
            
        