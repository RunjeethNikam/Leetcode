class Solution {
    public ListNode deleteMiddle(ListNode head) {
        ListNode dummyNode = new ListNode(-1, head);
        ListNode prev = dummyNode;
        ListNode fast = head, slow = head;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        prev.next = slow.next;

        return dummyNode.next;
    }
}