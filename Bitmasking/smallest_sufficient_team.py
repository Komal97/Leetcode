'''
https://leetcode.com/problems/smallest-sufficient-team/
In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.
Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. 
We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person.
You may return the answer in any order.  It is guaranteed an answer exists.
Example 1:
Input: 
req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: 
[0,2]
'''

from collections import defaultdict
class Solution:
    def findTeam(self, mask, maskpeople, i, soln, nskills, finalsol):
        if i == len(maskpeople):
            if (mask == (1<<nskills)-1):                                            # if all bits are set, means all skills are covered
                if len(finalsol[0]) == 0 or len(finalsol[0]) > len(soln):
                    finalsol[0] = soln.copy()
            return
        
        
        self.findTeam(mask, maskpeople, i+1, soln, nskills, finalsol)               # if person is not consider
        soln.append(i)
        self.findTeam(mask|maskpeople[i], maskpeople, i+1, soln, nskills, finalsol) # if person is consider
        soln.pop()
        
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        h = defaultdict(int)
        for i, skill in enumerate(req_skills):
            h[skill] = i                                                            # create a skills map with bit number
            
        npeople = len(people)
        maskpeople = [0]*npeople
        
        for i in range(npeople):
            for j in range(len(people[i])):
                maskpeople[i] |= (1<<h[people[i][j]])                               # for each person, set bit corresponding to skill
        soln = []
        finalsol = [[]]
        self.findTeam(0, maskpeople, 0, soln, len(req_skills), finalsol)
        return finalsol[0]