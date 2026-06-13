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
        copyMap = {None:None} #old,new

        curr = head
        while curr:
            copy = Node(curr.val)
            copyMap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            node = copyMap[curr]
            node.next = copyMap[curr.next]
            node.random = copyMap[curr.random]
            curr = curr.next

        return copyMap[head]        


        


        