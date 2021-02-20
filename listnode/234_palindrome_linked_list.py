from ListNode import ListNode


class Solution:

    def isPalindrome(self, head: ListNode):
        """
        Reverse linked list first, then compare with original
        """
        if not head:
            return True 
        ori = []
        def help(h):
            ori.append(h.val)
            if not h.next:
                return h
            last = help(h.next)
            h.next.next = h
            h.next = None
            return last
        
        re = help(head)
        while re:
            if re.val != ori[0]:
                return False
            re = re.next
            ori = ori[1:]
        return True

    def isPalindrome_2(self, head: ListNode):
        left = head

        def help(right: ListNode):
            """
            Postorder traversal, using two pointers
            """
            nonlocal left
            if right is None:
                return True
            res = help(right.next)
            print(f' {left.val, right.val}')
            res = res and (left.val == right.val)
            left = left.next
            return res

        return help(head)

    def isPalindrome_3(self, head: ListNode):
        slow = fast = head
        # get mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # odd situation, need to move one more step
        if not fast is None:
            slow = slow.next
        
        def help(node):
            pre = None
            cur = node
            while not cur is None:
                cur.next, cur, pre = pre, cur.next, cur
            return pre
        
        left = help(slow)
        right = head
        while right and left:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True


nums = [1, 1, 2, 1]
nums = [1, 1, 1]
nodes = [ListNode(val=a) for a in nums]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

test = Solution()
# res = test.isPalindrome(head)
# res = test.isPalindrome_2(head)
res = test.isPalindrome_3(head)
print(res)