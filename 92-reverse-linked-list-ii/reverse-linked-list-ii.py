# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        leftNode,rightNode = None, None
        bleftNode,arightNode = None, None
        i = 1
        curr = dummy
        while not rightNode:
            if not leftNode and i == left:
                leftNode = curr.next
                bleftNode = curr
            if i - 1 == right:
                rightNode = curr
                arightNode = curr.next
            i+=1
            curr = curr.next

        bleftNode.next,rightNode.next = None, None
        prev,curr = None, leftNode

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        bleftNode.next = rightNode
        leftNode.next = arightNode

        return dummy.next


