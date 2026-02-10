# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        curr1, curr2 = head,prev

        #1 -> 2 -> 3
        #5 -> 4

        while curr1 and curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2

        return head
            
            

            
            
            

