class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        i = 0, j = len(tmp) - 1
        while i < j:
            if tmp[i] != tmp[j]:
                return False
            i += 1
            j -= 1
        return True