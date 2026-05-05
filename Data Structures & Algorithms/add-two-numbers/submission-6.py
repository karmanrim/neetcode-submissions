# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        next_plus_digit = 0
        while l1 or l2:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            all_val = l1_val + l2_val + next_plus_digit
            cur_digit = all_val % 10
            next_plus_digit = all_val // 10
            node.next = ListNode(cur_digit)
            node = node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if next_plus_digit != 0:
            node.next = ListNode(next_plus_digit)
        return res.next