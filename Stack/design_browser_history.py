'''
https://leetcode.com/problems/design-browser-history/
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
Implement the BrowserHistory class:
BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
'''

# method - 1, keep 2 stacks - backward and forward
# while moving back, pop from back and add in forward and return from backward top
# while moving forward, pop from forward and add in backward and return from backward top
class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.backward = [homepage]
        self.forwarding = []

    def visit(self, url: str):
        self.backward.append(url)
        self.forwarding = []
        
    def back(self, steps: int):
        while len(self.backward)>1 and steps>0:
            val = self.backward.pop()
            self.forwarding.append(val)
            steps -= 1
        
        return self.backward[-1] if len(self.backward) > 0 else self.forwarding[-1]

    def forward(self, steps: int):
        
        while len(self.forwarding)>0 and steps>0:
            val = self.forwarding.pop()
            self.backward.append(val)
            steps -= 1

        return self.backward[-1] 

# method - 2, use Doubly Linked List
class BrowserHistory:
    
    class Node:
        def __init__(self, url):
            self.url = url
            self.next = None
            self.prev = None
            
    def __init__(self, homepage: str):
        self.head = self.Node(homepage)
        self.tail = self.head
        self.cur = self.head
    
    def visit(self, url: str):
        
        n = self.Node(url)
        self.cur.next = n
        n.prev = self.cur
        self.cur = n
        self.tail = n
        
    def back(self, steps: int):
        
        while self.cur.prev and steps:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url
        
    def forward(self, steps: int):
        
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


