# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        
        def check(head,k):
            left = 0
            temp = head
            while temp:
                left += 1
                temp = temp.next
                if left == k:
                    return True
            return False
        
        i = 0
        prev = None
        current = new_head.next
        temp_head = new_head
        while True:
            tail = current
            if check(current, k) == False:
                temp_head.next = tail
                break
            while i < k and current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                i += 1
            temp_head.next = prev
            temp_head = tail
            prev = None
            i = 0
        return new_head.next