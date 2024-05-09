class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode dummyNode = new ListNode(-1, list1);
        ListNode prev = dummyNode;
        ListNode curr = list1;
        for (int index = 0; index < b+1; index++) {
            if (index == a){
                prev.next = list2;
            }
            prev = curr;
            curr = curr.next;
        }

        while (list2.next != null) {
            list2 = list2.next;
        }
        list2.next = curr;
        return dummyNode.next;

    }
}
