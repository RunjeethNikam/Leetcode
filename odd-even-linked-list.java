/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode h1 = null, h2 = null, t1 = null, t2 = null;
        int count = 0;
        ListNode curr = head;
        while (curr != null) {
            ListNode nxt = curr.next;
            curr.next = null;

            if ((count % 2) == 0) {
                if (h1 == null) {
                    h1 = curr;
                    t1 = curr;
                } else {
                    t1.next = curr;
                    t1 = t1.next;
                }
            } else {
                if (h2 == null) {
                    h2 = curr;
                    t2 = curr;
                } else {
                    t2.next = curr;
                    t2 = t2.next;
                }
            }


            curr = nxt;
            count++;
        }

        t1.next = h2;
        return h1;
    }
}