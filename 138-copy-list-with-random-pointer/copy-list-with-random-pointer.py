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
        mapList = {None:None}

        curr = head

        while curr:
            new = Node(x = curr.val)
            mapList[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            copy = mapList[curr]
            copy.next = mapList[curr.next]
            copy.random = mapList[curr.random]
            curr = curr.next
        
        return mapList[head]

        

    
        