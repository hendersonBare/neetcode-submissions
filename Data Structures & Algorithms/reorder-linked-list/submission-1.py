# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = {}
        i = -1
        ptr = head
        while(ptr):
            i+=1
            nodes[i] = ptr
            ptr = ptr.next
        print(nodes)
        j = 0
        ptr = head
        nxt = head.next
        print(i)
        while (j<i//2):
            temp = nodes[i-j]
            if (i-j-1)>0:
                nodes[i-j-1].next = None
            ptr.next = temp
            temp.next = nxt
            ptr=nxt
            if nxt:
                nxt=nxt.next
            j+=1
        return


