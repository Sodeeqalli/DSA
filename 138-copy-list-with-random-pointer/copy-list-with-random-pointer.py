"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        new = Node(0)
        dummy = new
        curr = head
        oldNewPair = {}
        while curr:
            dummy.next = Node(curr.val)
            oldNewPair[curr] = dummy.next
            dummy = dummy.next
            curr = curr.next

        newCurr = new.next
        oldCurr = head
        while newCurr:
            if oldCurr.random:
                newCurr.random = oldNewPair[oldCurr.random]
            oldCurr = oldCurr.next
            newCurr = newCurr.next
        
        return new.next

            




        