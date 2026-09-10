# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            new_list = []
            for i in range(0,len(lists),2):
                if i == len(lists) -1:
                    new_list.append(lists[i])
                else:
                    res = self.mergeTwoLists(lists[i],lists[i+1])
                    new_list.append(res)
            lists = new_list
        
        return lists[0]


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = head = ListNode(0,None)

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                dummy.next = list1
                list1=list1.next
                dummy=dummy.next
            else:
                dummy.next = list2
                list2=list2.next
                dummy=dummy.next

        dummy.next = list1 or list2

        return head.next