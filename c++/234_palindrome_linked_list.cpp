/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* temp;
    bool isPalindrome(ListNode* head) {
        temp = head;
        return check(head);
    }
    bool check(ListNode* p) {
        if (NULL == p) return true;
        bool res = check(p->next) & (p->val == temp->val);
        temp = temp->next;
        return res;
    }

    ListNode* reverse(ListNode* p) {
        // reverse a linked list
        if (!p) return NULL;
        ListNode* pre = NULL;
        ListNode* temp = p;
        while (p) {
            temp = p->next;
            p->next = pre;
            pre = p;
            p = temp;
        }
        return pre;
    }

    bool isPalindrome2(ListNode* root) {
        if (!root) return true;
        ListNode* slow = root;
        ListNode* fast = root;
        while (fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        // reverse the second half
        slow->next = reverse(slow->next);
        slow = slow->next;
        while (slow) {
            if (slow->val != root->val) {
                return false;
            }
            else {
                slow = slow->next;
                root = root->next;
            }
        return true;

    }

    bool isPalindrome3(ListNode* root) {
        if (!root) return true;
        ListNode* fast = root;
        ListNode* slow = root;
        ListNode* rev = NULL;
        ListNode* temp = NULL;
        ListNode* temp2 = NULL;

        while (fast && fast->next) {
            fast = fast->next->next;
            // reverse the first half of linked list, be careful!
            temp = slow->next;
            temp2 = rev;
            rev = slow;
            rev.next = temp2;
            slow = temp;
        }
        if (fast) {
            slow = slow->next;
        }
        while (rev) {
            if (rev->val != slow->val) return false;
            rev = rev->next;
            slow = slow->next;
        }
        return true;
    }
};