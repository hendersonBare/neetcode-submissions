# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr1,ptr2=head,head.next
        while ptr2 is not None and ptr2.next is not None:
            ptr1=ptr1.next
            ptr2=ptr2.next.next or None
        
        prev,nxt = ptr1,ptr1.next
        prev.next = None
        while prev is not None and nxt is not None:
            tmp=nxt.next
            nxt.next=prev
            prev=nxt
            nxt=tmp

        beg,end=head,prev
        while beg is not None and end is not None:
            tmpb=beg.next
            beg.next=end
            beg=tmpb

            tmpe=end.next
            end.next=beg
            end=tmpe

        return

