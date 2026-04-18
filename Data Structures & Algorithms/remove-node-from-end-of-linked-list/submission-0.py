# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        num_nodes = 0
        curr = head
        while curr:
            num_nodes += 1
            curr = curr.next
            
        idx_to_remove = num_nodes - n
        idx = 1
        curr = head
        while curr:
            if idx == idx_to_remove:
                temp = curr.next.next
                curr.next = temp
                curr = temp
            else:
                curr = curr.next
            idx += 1
        return head
