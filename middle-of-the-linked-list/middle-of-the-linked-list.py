# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        curr = head.next
        while curr.next and curr.next.next:
            head = head.next
            curr = curr.next.next
        return head.next
        