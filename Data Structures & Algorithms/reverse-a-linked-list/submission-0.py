# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        head = stack.pop()
        res = head
        i = len(stack)-1
        while i>=0:
            node =  stack.pop()
            head.next = node
            i-=1
            head = head.next
        head.next =None
        return res