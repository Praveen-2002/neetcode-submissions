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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }
        int l = 0, r = lists.length -1;
        return divide(lists, l, r);
    }

    private ListNode divide(ListNode[] list, int left, int right){
        int mid = (left +right)/2;
        if (left > right || right < left){
            return null;
        }
        if (left == right){
            return list[left];
        }
        ListNode leftNode = divide(list, left, mid);
        ListNode rightNode = divide(list, mid +1, right);

        return combine(leftNode, rightNode);
    }

    private ListNode combine(ListNode left, ListNode right){
        ListNode merged = new ListNode(1);
        var temp = merged;
        while (left != null && right != null){
            if (left.val < right.val){
                merged.next = new ListNode(left.val);
                left = left.next;
            }
            else{
                merged.next = new ListNode(right.val);
                right = right.next;
            }
            merged = merged.next;
        }
        if(left != null){
            merged.next  = left;
        }
        else if(right != null){
            merged.next = right;
        }
        return temp.next;
    }
}
