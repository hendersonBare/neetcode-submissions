# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 1
        ptr = head
        while(ptr.next is not None):
            length += 1
            ptr = ptr.next

        if length == 1:
            return None

        if length - n == 0:
            return head.next

        start = head
        for i in range(length-n-1):
            start = start.next #this takes start to the node before the one to be removed


        print(start.val)

        if start.next is not None and start.next.next is not None:
            start.next = start.next.next
            
        else:
            start.next = None

        return head
