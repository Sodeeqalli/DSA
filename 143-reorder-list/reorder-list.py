# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next , head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev, curr = None, slow.next
        slow.next = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        part1, part2 = head, prev

        while part2:
            store1 = None if not part1 else part1.next
            part1.next = part2
            store2 = None if not part2 else part2.next
            part2.next = store1
            part1 = store1
            part2 = store2
        
        return head


            
        
        