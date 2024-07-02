'''
https://leetcode.com/problems/reorder-list/description/
Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the nodes' values.
Input:

2
3
1 2 3
4
1 7 3 4

Output:
1 3 2
1 4 7 3
'''

# divide list into 2 halves, reverse second half and then connect 2 list
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def midPoint(node):
            s = node
            f = node.next

            while f and f.next:
                f = f.next.next
                s = s.next
            
            return s

        def reverse(node):
            prev = None
            c = node

            while c:
                n = c.next
                c.next = prev
                prev = c
                c = n
            return prev

        if not head or not head.next:
            return head

        a = head
        mid = midPoint(head)
        b = mid.next
        mid.next = None
        b = reverse(b)

        while a or b:
            if a:
                temp = a.next
                a.next = b
                a = temp
            if b:
                temp = b.next
                b.next = a
                b = temp

        