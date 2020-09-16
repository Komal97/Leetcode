'''
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note: All numbers (including target) will be positive integers. The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n, ans, _ = len(candidates), [], candidates.sort()    
        
        def findCombo(summ, path, idx):
            
            if summ == target:
                ans.append(path)
                return
		
            for i in range(idx, n):
                # at first level idx = 0 but after completing left, we pop 1 at 0th pos and 1 at 1st pos but we dont have to traverse 1 again
                if i > idx and candidates[i] == candidates[i-1]:            
                    continue
                if summ+candidates[i] > target:
                    break
                findCombo(summ+candidates[i], path + [candidates[i]], i + 1)
        
        findCombo(0, [], 0)
        return ans