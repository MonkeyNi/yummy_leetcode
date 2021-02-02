# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        l = r = head
        while r and r.next:
            r = r.next.next
            l = l.next
            if l == r:
                break
        else:
            return None
        while head != l:
            head = head.next
            l = l.next
        return l