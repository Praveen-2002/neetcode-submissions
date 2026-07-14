# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = [head]
        temp = head.next
        while temp:
            stack.append(temp)
            temp = temp.next
        top_node = stack[0]
        right = True
        ind = 1
        added = 1
        n = len(stack)
        while ind <= n//2 and added<n:
            val = None
            if right:
                val = stack[n-ind]
            else:
                val = stack[ind]
                ind+=1
            right = not right
            top_node.next = val
            top_node = val
            added+=1
        top_node.next = None
        