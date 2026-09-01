# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        ptr = head
        while ptr is not None:
            nodes.append(ptr)
            ptr=ptr.next

        l,r=0,len(nodes)-1

        while (r-l>1):
            nodes[l].next=nodes[r]
            l+=1
            nodes[r].next=nodes[l]
            r-=1

        if len(nodes)%2==1:
            nodes[l].next=None
        else:
            nodes[l].next=nodes[r]
            nodes[r].next=None

        return