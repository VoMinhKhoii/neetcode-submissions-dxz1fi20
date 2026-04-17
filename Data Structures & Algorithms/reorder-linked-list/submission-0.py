# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find mid point
        # Reverse second half
        # Merge two list
        if head.next == None:
            return None
        fast, slow = head, head
        mid = ListNode()

        # Find mid
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # Here we have head, and mid
        # Cut the list
        start_second = slow.next
        slow.next = None

        # Now reverse from mid.
        prev, curr = None, start_second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Now the reversed of second list start at prev.
        dummy = head
        while head != None and prev != None:
            temp_1 = head.next
            temp_2 = prev.next
            head.next = prev
            prev.next = temp_1
            head = temp_1
            prev=temp_2
        return None

