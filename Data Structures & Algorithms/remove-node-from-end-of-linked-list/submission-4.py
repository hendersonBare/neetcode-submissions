# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        nodes = 0
        while ptr is not None:
            nodes += 1
            ptr = ptr.next
        
        if nodes <= 1:
            return None
        elif n == nodes:
            head=head.next
            return head

        else:
            ptr = head
            curr = 1
            while nodes - curr != n:
                ptr = ptr.next
                curr += 1
            
            ptr.next = ptr.next.next
            return head
                