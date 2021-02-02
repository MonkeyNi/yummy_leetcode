# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l = r = head
        while r and r.next:
            r = r.next.next
            l = l.next
            if l == r:
                return True
        return False
