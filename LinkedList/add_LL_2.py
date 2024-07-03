'''
https://leetcode.com/problems/add-two-numbers-ii/
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# keep position of numbers 
# add number with same position only
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def length(node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count

        def addTwoNumbersHelper(l1, len1, l2, len2, temp):
            if len1 == 0 and len2 == 0:
                return 0
            
            data = 0
            oc = 0
            if len1 > len2:
                oc = addTwoNumbersHelper(l1.next, len1-1, l2, len2, temp.next)
                data = oc + l1.val
            elif len1 < len2:
                oc = addTwoNumbersHelper(l1, len1, l2.next, len2-1, temp.next)
                data = oc + l2.val
            else:
                oc = addTwoNumbersHelper(l1.next, len1-1, l2.next, len2-1, temp.next)
                data = oc + l1.val + l2.val

            temp.val = data % 10
            nc = data // 10
            return nc


        len1 = length(l1)
        len2 = length(l2)
        head = l1 if len1 > len2 else l2
        temp = head
        c = addTwoNumbersHelper(l1, len1, l2, len2, temp)
        if c > 0:
            n = ListNode(c)
            n.next = head
            head = n
        return head

        
        
        