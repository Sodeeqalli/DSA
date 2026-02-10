# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        dummy = ListNode()
        dummy.next = prev
        curr = dummy
        counter = 1
        while counter < n:
            curr = curr.next
            counter+=1
        
        curr.next = curr.next.next

        prev, curr = None, dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

        