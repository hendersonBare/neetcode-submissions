# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = 0
        mult = 1
        while(l1 is not None):
            l1_num += l1.val * mult
            mult *= 10
            l1 = l1.next

        l2_num = 0
        mult = 1
        while(l2 is not None):
            l2_num += l2.val * mult
            mult *= 10
            l2 = l2.next

        print(l1_num)
        print(l2_num)

        fin_num = l1_num + l2_num
        new_head = ListNode()
        new_ptr = new_head
        mult = 10
        for i in range(len(str(fin_num))-1):
            value = fin_num % mult
            new_ptr.val = value
            fin_num = (fin_num - value) // mult
            new_ptr.next = ListNode()
            new_ptr = new_ptr.next
        new_ptr.val = fin_num % mult
        return new_head
