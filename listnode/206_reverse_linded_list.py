# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # standard method
        pre = None
        while head:
            cur = head
            # head is the middle vaiable
            head = head.next
            cur.next = pre
            pre = cur
        return pre
    
    def reverseList2(self, head: ListNode) -> ListNode:
        # revursive method
        if not head:
            return head
        if head.next == None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last