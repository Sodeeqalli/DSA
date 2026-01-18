# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 ->5
        dummy = ListNode(-1,head)
        curr = dummy
        position = 0
        leftNode, rightNode = None,None
        beforeLeft, afterRight = None,None

        while curr.next:
            if position == left - 1:
                leftNode = curr.next
                beforeLeft = curr
            if position == right - 1:
                rightNode = curr.next
                afterRight = curr.next.next
            curr = curr.next
            position+=1
        
        rightNode.next = None
        
        headReversed = leftNode
        prev,curr = None, headReversed

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        begin = prev
        end = leftNode

        beforeLeft.next = begin
        end.next = afterRight

        return dummy.next


        