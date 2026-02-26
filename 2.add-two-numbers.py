#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        node = head
        excess = 0

        while l1 or l2 or excess:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + excess
            excess = int(sum / 10)

            l = ListNode(sum % 10, None)
            node.next = l
            node = node.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next