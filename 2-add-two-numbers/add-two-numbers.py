# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0

        dummy = ListNode()
        curr3 = dummy

        while curr1 or curr2 or carry:
            value = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
            curr3.next = ListNode(val = value % 10)
            carry = value // 10
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            curr3 = curr3.next

        return dummy.next
        




