/**

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

/*
Inputs: l1 and l2, linked lists with single digit integer values at each node
Outputs: Result, integer added up of the reversed numbers from the linked lists digits.
Axioms: 
    - Linked lists wont be empty
    - Digits will be >= 0
    - Singly linked lists
Approach:
    - Go through each linked list once at the same time
    - As you cycle through the lists, add the val's together and if they are greater than 10, subtract 10 and set int carryOver to 1
    - At next value for both lists, if carryOver is 1, we add +1 to the normal l1.val + l2.val calculation
    - Repeat this till we reach the end of one or both linked lists at the same time
    - Then we just continue on with the remaining linked list and keep moving our new vals to l3. at the end we return l3
Run Time: O(n+m)
Space Complexity: O(1)


*/
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(0);
        ListNode curr1 = l1;
        ListNode curr2 = l2;
        ListNode curr3 = l3;
        int carryOver = 0;
        
        while(curr1 != null && curr2 != null){
            curr3.val = curr1.val + curr2.val + carryOver;
            carryOver = 0;
            if (curr3.val > 9){
                carryOver = 1;
                curr3.val -= 10;
            }
            curr1 = curr1.next;
            curr2 = curr2.next;
            if(curr1 == null && curr2 == null && carryOver == 0){
                return l3;
            } else if(curr1 == null && curr2 == null && carryOver == 1){
                curr3.next = new ListNode(1);
                return l3;
            } else {
                curr3.next = new ListNode(0);
                curr3 = curr3.next;
            }

        }
        
        if (curr1 == null){
            leftOver(curr2, curr3, carryOver);
            return l3;
        } else{
            leftOver(curr1, curr3, carryOver);
            return l3;
        }
        
    }
    
     public void leftOver(ListNode remain, ListNode l3, int carryOver) {
         while(remain!= null){
             l3.val = remain.val + carryOver;
             
             if (l3.val > 9){
                carryOver = 1;
                l3.val -= 10;
             }else{
                carryOver = 0;
             }
             
             remain = remain.next;
             if(remain == null && carryOver == 0){
                 return;
                 
             }else if(remain == null && carryOver == 1){
                 l3.next = new ListNode(1);
             } else{
                 l3.next = new ListNode(0);
                 l3 = l3.next;
             }
         }
         
         return;
     }
}
