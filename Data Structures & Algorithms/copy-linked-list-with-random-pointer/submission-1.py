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
        node_map = {}
        if head is None:
            return None
        head_ptr = head
        while head_ptr is not None:
            node_map[head_ptr] = Node(head_ptr.val, None, None)
            head_ptr = head_ptr.next
    
        new_head = node_map[head]
        new_ptr = new_head
        ptr = head

        while new_ptr is not None and ptr is not None:
            if ptr.next:
                new_ptr.next = node_map.get(ptr.next, None)
            else:
                new_ptr.next = None
            if ptr.random:
                new_ptr.random = node_map.get(ptr.random, None)
            else:
                new_ptr.random = None

            new_ptr = new_ptr.next
            ptr = ptr.next

        return new_head