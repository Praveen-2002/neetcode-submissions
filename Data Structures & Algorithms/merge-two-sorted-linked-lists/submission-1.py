# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        while list1 or list2:
            node = None
            if list2 == None or (list1 and list1.val < list2.val):
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            res.next = node
            res = res.next
        return temp.next
