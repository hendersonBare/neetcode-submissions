# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        if not ptr:
            return None
        nxt = ptr.next
        ptr.next = None
        while (nxt):
            temp = nxt.next
            nxt.next = ptr
            ptr = nxt
            nxt = temp
            print(ptr.next.val)
        return ptr