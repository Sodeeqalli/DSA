# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr1, curr2, curr3 = l1, l2, l3
        carry = 0

        while curr1 or curr2 or carry:
            res = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
            carry = 0
            if res >= 10:
                carry = 1
                res -= 10
            curr3.next = ListNode(res)
            curr3 = curr3.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        return l3.next

            


        
        