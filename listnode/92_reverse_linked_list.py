# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode


class Solution:
    
    def __init__(self,):
        self.successor = ListNode()
        
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head.next == None or left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
    
    def reverseN(self, head, right):
        if head.next == None or right == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, right-1)
        head.next.next = head
        head.next = self.successor
        return last
    
    
nums = [1, 2, 3, 4, 5, 6]
nodes = [ListNode(val=a) for a in nums]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

test = Solution()
# print('Original List: ')
# while head:
#     print(head.val)
#     head = head.next
res = test.reverseBetween(head, 2, 4)
print('Reversed List:')
while res:
    print(res.val)
    res = res.next
