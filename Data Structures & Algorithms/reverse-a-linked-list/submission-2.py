# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prv = head
        nxt = head.next
        prv.next = None

        while nxt is not None:
            temp = nxt.next
            nxt.next = prv
            prv = nxt
            nxt = temp

        return prv


        