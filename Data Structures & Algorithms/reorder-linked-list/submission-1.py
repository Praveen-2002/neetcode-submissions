# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        i = slow.next # 1st of the right list
        if i == None: return
        j = slow.next.next

        while i and j:
            t = j.next
            j.next = i
            i = j
            j = t
        slow.next.next = None

        left, right = head, i
        back = True
        while left and right:
            if back or not left:
                t = left.next
                left.next  = right
                left = t
            else:
                t = right.next
                right.next = left
                right = t
            back = not back
        if right:
            right.next = None
        if left:
            left.next = None

        
            
