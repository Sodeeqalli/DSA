# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse
        #add dummy
        #remove
        #reverse

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        dummy = ListNode()
        dummy.next = prev

        curr = dummy
        i = 1
        while i < n:
            i+=1
            curr = curr.next
        curr.next = curr.next.next

        prev, curr = None, dummy.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

        