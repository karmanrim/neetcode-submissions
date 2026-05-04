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
        hmap = {None: None}
        tmp = head
        while tmp:
            hmap[tmp] = Node(tmp.val)
            tmp = tmp.next
        tmp = head
        while tmp:
            hmap[tmp].next = hmap[tmp.next]
            hmap[tmp].random = hmap[tmp.random]
            tmp = tmp.next
        return hmap[head]

