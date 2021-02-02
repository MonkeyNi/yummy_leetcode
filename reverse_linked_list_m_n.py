# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Step 1: reverse a list by recursion;
    Step 2: reverse pre n listnode by recursion; (remember successor)
    Step 3: reverse m to n listnode by recursion;
    """
    def init(self):
        self.successor = None

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head 
        # pass

    def reverseN(self, head, m):
        if m == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, m-1)
        head.next.next = head
        head.next = self.successor
        return last

        