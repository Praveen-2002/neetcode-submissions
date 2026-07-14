# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        slow = head.next
        fast = head.next.next
        while fast != None and slow != fast:
            if fast.next == None:
                break
            slow = slow.next
            fast = fast.next.next
        return slow == fast