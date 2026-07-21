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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        int len = 0;

        while (temp != null){
            temp = temp.next;
            len += 1;
        };

        int index = len - n;
        System.out.println(index);
        if (index == 0){
            return head.next;
        }
        var res = head;
        var prev = head;
        while (index > 0){
            prev = head;
            head = head.next;
            index -=1;
        }
        prev.next = head.next;
        return res;
    }
}
