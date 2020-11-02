'''
https://leetcode.com/problems/insertion-sort-list/
Sort a linked list using insertion sort.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head: ListNode):
        if not head or not head.next:
            return head
        
        prev = head
        temp = head.next
        
        while temp:
            # if current element is greater than or equal to prev then continue
            if temp.val >= prev.val:
                prev = temp
                temp = temp.next
            # else 2 options: insertion either at head or in between
            else:
                # separate out node
                prev.next = temp.next
                temp.next = None
                # check head, if satisfy then insert at head and update head
                if head.val >= temp.val:
                    temp.next = head
                    head = temp
                # else insert in middle
                else:
                    start = head
                    while start.next and start.next.val < temp.val:
                        start = start.next
                    temp.next = start.next
                    start.next = temp
                temp = prev.next
            
        return head