# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return -1
        slow, fast = head.next, head.next.next
        while slow != None and fast != None:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
        return False