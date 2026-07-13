# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        curr_node = head.next
        head.next = None
        while curr_node:
            temp = curr_node
            curr_temp = curr_node.next
            curr_node.next = head
            head = temp
            curr_node = curr_temp
        return head