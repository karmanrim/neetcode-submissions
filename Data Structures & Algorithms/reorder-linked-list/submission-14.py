# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_mid(self, p):
        slow, fast = p, p.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow
        slow = slow.next
        tmp.next = None
        return slow
    
    def reverse_list(self, p):
        cur = p
        prev = None
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_mid(head)
        reverse_p = self.reverse_list(mid)
        dummy = node = ListNode()
        while head and reverse_p:
            node.next = head
            head = head.next
            node = node.next
            node.next = reverse_p
            reverse_p = reverse_p.next
            node = node.next
        node.next = head









