# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr1, curr2, curr3, cover = l1, l2, dummy, 0

        while curr1 or curr2 or cover:
            value = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + cover
            cover = 0
            if value >= 10:
                cover = 1
                value = value - 10
            curr3.next = ListNode(value)
            curr3 = curr3.next
            curr1 = None if not curr1 else curr1.next
            curr2 = None if not curr2 else curr2.next
        
        return dummy.next


        