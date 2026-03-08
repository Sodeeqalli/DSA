# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        before = dummy
        curr = start = head
        i = 1
        while curr:
            if i == 1:
                start = curr
            if i == k:
                after = curr.next
                curr.next = None
                self.reverse(before,start,after)
                before = start
                curr = after
                i = 1
                continue
            i+=1
            curr = curr.next
        
        return dummy.next

    def reverse(self,before,start,after):
        prev, curr = None, start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        start.next = after
        before.next = prev

        





        