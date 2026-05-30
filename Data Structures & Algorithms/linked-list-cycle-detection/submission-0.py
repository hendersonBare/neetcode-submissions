# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = {}
        while node.next:
            if node in visited:
                return True
            visited[node] = 1
            node = node.next
        return False
