# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elements = []
        curr = head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        
        headReversed = ListNode(elements.pop())
        curr = headReversed
        while elements:
            curr.next = ListNode(elements.pop())
            curr = curr.next
        
        return headReversed


        