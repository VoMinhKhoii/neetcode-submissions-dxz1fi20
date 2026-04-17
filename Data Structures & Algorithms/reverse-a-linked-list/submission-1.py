# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a -> b -> c -> d -> NONE
        # res: d -> c -> b -> a 

        # ITERATIVE
        # prev , curr = None, head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev

        #     prev = curr
        #     curr = temp
        # return prev        

        # RECURSION 
        if not head or not head.next:
            return head
        # Imagine we have 5 nodes, then at last step, new_head is node 5, head is node 4
        # so head.next is node 5
        # Remember at base case, we return directly, not add to the stack anymore
        # So the first to be popped out, is second to last, not last
        # --> head.next.next = None
        # AFTER RECURSION RETURN, WE NEED: head.next.next = head
        new_head = self.reverseList(head.next)

        head.next.next = head
        # If just head.next.next = head, 5 now points to 4, but 4 still points to 5
        head.next = None
        return new_head