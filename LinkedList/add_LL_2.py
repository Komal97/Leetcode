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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        
        def length(head):
            count = 0
            while head:
                head = head.next
                count += 1
            return count
        
        def add(head1, lh1, head2, lh2, temp):
            nonlocal carry
            
            if lh1 == 0 and lh2 == 0:
                return
            
            if lh1 > lh2:
                add(head1.next, lh1-1, head2, lh2, temp.next)
            elif lh1 < lh2:
                add(head1, lh1, head2.next, lh2-1, temp.next)
            else:
                add(head1.next, lh1-1, head2.next, lh2-1, temp.next)
                
            summ = (head1.val if lh1 >= lh2 else 0) + (head2.val if lh1 <= lh2 else 0) + carry
            temp.val = summ%10
            carry = summ//10
                
        
        lh1 = length(l1)
        lh2 = length(l2)
        
        head = l1 if lh1 > lh2 else l2
        temp = head
        carry = 0
        
        add(l1, lh1, l2, lh2, temp)
        
        if carry > 0:
            n = ListNode(carry)
            n.next = head
            head = n
        return head
        
        
        