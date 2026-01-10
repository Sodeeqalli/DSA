# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondhead = slow.next
        slow.next = None
        prev,curr = None, secondhead
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tail = prev
        
        #1->2->3
        #5->4
        while tail:
            tmp1,tmp2 = head.next,tail.next
            head.next = tail
            tail.next = tmp1
            head,tail = tmp1,tmp2

    


            
            

        # 1 -> 2 -> 3 <- 4

        # 1 -> 4 -> 2 ->3

        #1 ->2 -> 3 ->4 -> 5
        
        #store 2
        # 1.next = 4
        #store 3
        # 4.next = 2
        #store 3
        #2.next = 3
        
        #store 2
        #1.next = 5
        #store 4
        #5.next = 2
        #store 3
        #2.next = 4
        

            
            


        


        