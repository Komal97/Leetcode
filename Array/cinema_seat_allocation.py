'''
https://leetcode.com/problems/cinema-seat-allocation/
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.
Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.
Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, 
but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

Example 1:
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.

Example 2:
Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example 3:
Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
'''

from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]):                                                              
        group = set()
        rows = set()
        count = 0
        for row, col in reservedSeats:
            group.add((row, col))
            rows.add(row)
        
        # there are 3 options (but there is overlapping in them)
        # for left = 2,3,4,5
        # for middle = 4,5,6,7
        # for right = 6,7,8,9
        for row in rows:        # if we run from 1 to n then TLE       
            left = ((row, 2) not in group) and ((row, 3) not in group) and ((row, 4) not in group) and ((row, 5) not in group)
            middle = ((row, 4) not in group) and ((row, 5) not in group) and ((row, 6) not in group) and ((row, 7) not in group)
            right = ((row, 6) not in group) and ((row, 7) not in group) and ((row, 8) not in group) and ((row, 9) not in group)
            
            if left and right:
                count += 2
            elif left or right or middle:
                count += 1
        
        # (n - len(rows))*2 =  remaining rows not in set and each contribute 2 pairs
        return count + ((n - len(rows))*2)
    
    
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]):                                                               
        reserved_map = defaultdict(int)
        
        # show each row as 10 bit number
        for row, col in reservedSeats:
            reserved_map[row] |= (1 << (10-col))
        
        count = 0
        
        right = 15 << 1        # 0000011110
        middle = 15 << 3       # 0001111000
        left = 15 << 5         # 0111100000
        
        for row in reserved_map:
            val = reserved_map[row]
            r =  val & right
            m = val & middle
            l = val & left
            
            if (l) == 0 and (r) == 0:
                count += 2
            elif (l) == 0 or (m) == 0 or (r) == 0:
                count += 1
        
        return count + (( n - len(reserved_map))*2)

