'''
https://leetcode.com/problems/word-ladder/
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time. Each transformed word must exist in the word list.
Note:
Return 0 if there is no such transformation sequence.
All words have the same length and contain only lowercase alphabetic characters.
You may assume no duplicates in the word list and beginWord and endWord are non-empty and are not the same.
Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

# to find min distance, use BFS
from collections import deque, defaultdict
class Solution:
    
    def findTransformations(self, word, visited, q, level):
        
        # word - hit
        # replace h with a-z and check new word in visited map, if yes means those are new neighbors of 'hit', 
        # in same way, replace i from a-z and t from a-z 
        s = list(word)
        
        for i in range(len(s)):
            ch = s[i]
            for j in range(26):
                char = chr(ord('a') + j)
                s[i] = char
                w = ''.join(s)
                if w in visited and visited[w] == False:
                    q.append([w, level+1])
            s[i] = ch
            
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]):
        
        if endWord not in wordList:
            return 0
        
        # create a visited map
        visited = {word: False for word in wordList}
        
        # append begin word (eg: hit)
        q = deque()
        q.append([beginWord, 1])

        while len(q) > 0:
            word, level = q.popleft()
            
            if word == endWord:
                return level
            if word in visited and visited[word]:
                continue
                
            visited[word] = True
            # find all transformations corresponding to hit
            self.findTransformations(word, visited, q, level)
        
        return 0