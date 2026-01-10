# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head = ListNode(next = prev)
        curr = head
        i = 1
        while curr.next:
            if i == n:
                curr.next = curr.next.next
                break
            curr = curr.next
            i += 1
        curr = head.next
        prev = None 
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev     
        
        