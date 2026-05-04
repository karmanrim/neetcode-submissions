# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp_head = head
        len_list = 0
        while tmp_head:
            len_list += 1
            tmp_head = tmp_head.next
        num_steps = len_list - n
        if len_list == 1:
            return None
        if num_steps == 0:
            return head.next
        tmp_head = head
        while num_steps > 1:
            tmp_head = tmp_head.next
            num_steps -= 1
        del_head = tmp_head.next
        tmp_head.next = del_head.next
        del_head.next = None
        return head