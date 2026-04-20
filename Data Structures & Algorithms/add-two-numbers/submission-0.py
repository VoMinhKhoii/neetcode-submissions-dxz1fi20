# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry_1 = False
        res = 0
        while l1 or l2 or carry_1 == True:
            if l1: 
                res = res + l1.val
                l1 = l1.next
            if l2: 
                res = res + l2.val
                l2 = l2.next

            if carry_1 == True:
                res = res + 1
            if res >= 10:
                res = res % 10
                carry_1 = True
            else:
                carry_1 = False
            curr.next = ListNode(res)
            curr = curr.next
            res = 0
        return head.next