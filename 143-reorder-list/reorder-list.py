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
        #get middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head1, head2 = head, prev

        while head1 and head1.next and head2:
            nxt1 = head1.next
            head1.next = head2
            nxt2 = head2.next
            head2.next = nxt1
            head1 = nxt1
            head2 = nxt2
        
        return head
        


        