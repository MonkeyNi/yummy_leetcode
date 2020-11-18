class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    successor = ListNode()
    
    def reverseN(head, n):
        if head.next == None:
            return head
        nonlocal successor
        if (n == 1):
            successor = head.next
        last = reverseN(head.next, n-1)
        head.next.next = head
        head.next = successor
        return last

    if (m == 1):
        return reverseN(head, n)
    head.next = reverseBetween(head.next, m-1, n-1)
    return head

dummy = head = ListNode()
for i in range(1,10):
    tmp = ListNode(val=i)
    dummy.next = tmp
    dummy = dummy.next

reverseBetween(head, 2, 5)
import pdb; pdb.set_trace()
