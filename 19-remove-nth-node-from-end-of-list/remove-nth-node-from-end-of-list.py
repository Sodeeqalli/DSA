# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        counter = 0
        curr = head
        while counter < n:
            curr = curr.next
            counter += 1
        
        left,right = dummy, curr

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

        