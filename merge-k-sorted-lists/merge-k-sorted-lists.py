# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [i for i in lists if i != None]
        if len(lists) == 0:
            return None
            
        output = temp = ListNode(0)
        l = []
        for i,n in enumerate(lists):
            head = n
            num = head.val
            lists[i] = lists[i].next
            l.append([num,i])
        heapq.heapify(l)
        while l != []:
            num, h = heapq.heappop(l)
            temp.val = num
            
            if lists[h] != None:
                num = lists[h].val
                heapq.heappush(l,[num,h])
                lists[h] = lists[h].next
            if l != []:
                tn = ListNode(0)
                temp.next = tn
                temp = temp.next
        return output
                
            
            
        
        