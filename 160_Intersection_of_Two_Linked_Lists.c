/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Suppose each linked list consists 2 parts, the second of which is the same as
// the counterpart of the other list. So walking through the 2 lists in different
// order will finally bring it to the condidion that the 2 pointers meet each other.
// If there is an intersection, it is exactly where they meet. Otherwise, they'll
// both point to null.

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {

    struct ListNode *a = headA;
    struct ListNode *b = headB;

    while(a != b){
        if(a)   a = a -> next;
        else a = headB;
        if(b)   b = b -> next;
        else b = headA;
    }

    return a;
}
