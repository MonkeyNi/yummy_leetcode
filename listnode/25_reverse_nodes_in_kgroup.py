# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        K = 1
        dummy = head
        while dummy.next:
            K += 1
            dummy = dummy.next
        n = K//k
        for tmp in range(n):
            i, j = 1+k*tmp, k*(tmp+1)
            head = self.reverse_n_m(head, i, j)
        return head
    
    def reverseK(self, head, k):
        successor = head
        
        def help(head, k):
            if  k == 1:
                successor = head.next
                return head
            last = help(head.next, k-1)
            head.next.next = head
            head.next = successor
            return last
        
        return help(head, k)
    
    def reverse_n_m(self, head, n, m):
        """
        revursive
        """
        if n == 1:
            return self.reverseK(head, m)
        head.next = self.reverse_n_m(head.next, n-1, m-1)
        return head
            
    
    def reverseKGroup_2(self, head: ListNode, k: int):
        """
        TLE: time limited exceeded
        """
        if not head:
            return head
        
        a = b = head
        
        for i in range(k):
            if not b:
                return head
            b = b.next
        
        last = self.reverse_n_m_2(a, b)
        a.next = self.reverseKGroup_2(b, k)
        return last
    
    def reverse_n_m_2(self, a: ListNode, b: ListNode):
        """
        iteration
        """
        pre = None
        cur = a
        while cur != b:
            cur.next, cur, pre = pre, cur.next, cur 
        return pre