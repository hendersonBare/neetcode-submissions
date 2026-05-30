# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = pointer = ListNode()
        ptr1, ptr2 = list1, list2
        while(ptr1 and ptr2):
            print("ptr1val: ", ptr1.val, " ptr2val: ",)
            if (ptr1.val < ptr2.val):
                pointer.next = ptr1#ListNode(ptr1.val, None)
                ptr1 = ptr1.next
            else:
                pointer.next = ptr2#ListNode(ptr2.val, None)
                ptr2 = ptr2.next
            pointer = pointer.next

        pointer.next = ptr1 if ptr1 is not None else ptr2
        return head.next
