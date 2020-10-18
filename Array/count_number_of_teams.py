'''
https://leetcode.com/problems/count-number-of-teams/
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4
'''

# take current element (j) as second person
# find number of people from left of j less than current and number of people greater than on right (j+1 to n)
# ans += (left * right) and so same for decreasing order (high from left and low from right)
class Solution:
    def numTeams(self, rating: List[int]):
        
        n = len(rating)
        
        count = 0
        for j in range(1, n-1):
            lowL, highL, lowR, highR = 0, 0, 0, 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    lowL += 1
                else:
                    highL += 1
            
            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    lowR += 1
                else:
                    highR += 1
            count += (lowL * highR) + (highL * lowR)
        
        return count