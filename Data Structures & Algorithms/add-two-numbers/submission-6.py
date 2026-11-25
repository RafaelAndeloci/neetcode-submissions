# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res

        carry = 0
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = s // 10
            rest = s % 10

            dummy.next = ListNode(rest)
            
            dummy = dummy.next 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
           

        return res.next