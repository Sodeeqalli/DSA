# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()

        carry = 0
        curr1, curr2, curr3 = l1,l2,l3
        while curr1 and curr2:
            addition = carry + curr1.val + curr2.val
            carry = 0
            if addition >= 10:
                carry += 1
                addition -= 10
            curr3.next = ListNode(addition)
            curr3 = curr3.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            addition = carry + curr1.val
            carry = 0
            if addition >= 10:
                carry+=1
                addition-=10
            curr3.next = ListNode(addition)
            curr3 = curr3.next
            curr1 = curr1.next

        while curr2:
            addition = carry + curr2.val
            carry = 0
            if addition >= 10:
                carry+=1
                addition-=10
            curr3.next = ListNode(addition)
            curr3 = curr3.next
            curr2 = curr2.next
        
        if carry > 0:
            curr3.next = ListNode(carry)
        
        return l3.next

        