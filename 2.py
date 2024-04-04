"""
2. Add Two Numbers
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        y = l2
        r = ListNode()
        n = 0
        c = r
        while x or y or n:
            vx = 0
            vy = 0
            if x:
                vx = x.val
                x = x.next
            if y:
                vy = y.val
                y = y.next
            m = vx + vy + n
            n = m//10
            c.val = m%10
            if not x and not y and not n:
                break
            c.next = ListNode()
            c = c.next
        return r

            
                

if __name__ == "__main__":
    x = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    y = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    z = Solution()
    z.addTwoNumbers(x, y)