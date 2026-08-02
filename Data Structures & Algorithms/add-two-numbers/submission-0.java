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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        var carry = -1;
        var res = new ListNode(0);
        var dummy = res;
        while (l1 != null && l2 != null){
            var val = carry < 0 ? l1.val + l2.val : l1.val + l2.val + carry;
            var passon = val/10;
            var remainder = val%10;
            if(passon <= 0){
                res.next = new ListNode(val);
                carry = -1;
            }
            else{
                res.next = new ListNode(remainder);
                carry = passon;
            }
            res = res.next;
            l1= l1.next;
            l2 = l2.next;
        }

        while(l1!= null){
            var val = carry <0 ? l1.val : l1.val+carry;
            var passon = val/10;
            var remainder = val%10;
            if(passon <= 0){
                res.next = new ListNode(val);
                carry = -1;
            }
            else{
                res.next = new ListNode(remainder);
                carry = passon;
            }
            res = res.next;
            l1 = l1.next;
        }
        while(l2!= null){
            var val = carry<0 ? l2.val : l2.val + carry;
            var passon = val/10;
            var remainder = val%10;
            if(passon <= 0){
                res.next = new ListNode(val);
                carry = -1;
            }
            else{
                res.next = new ListNode(remainder);
                carry = passon;
            }
            res = res.next;
            l2 = l2.next;
        }
        if (carry > -1){
            res.next = new ListNode(carry);
        }
        return dummy.next;
    }
}
