'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

# using doubly linked list and hashmap
from collections import defaultdict
class LRUCache:
    
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.next = None
            self.prev = None

    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.hash = defaultdict()

    # private functions
    def __insert(self, key: int, value: int):   
        
        # insert node in DLL at tail
        n = self.Node(key, value)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        
        # add key, node in hashmap
        self.hash[self.tail.key] = self.tail
        
    def __deleteAtBeg(self):            
        
        # delete node from head
        if self.head == None:
            return
        
        temp = self.head
        self.head = self.head.next
        if temp.next:
            temp.next.prev = None
        temp.next = None
        self.hash.pop(temp.key)
    
    def __deleteInMiddle(self, node):   
        
        # delete node from middle
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        
        # remove node from hashmap
        self.hash.pop(node.key)
        
    def get(self, key: int):
        
        # if key not present return -1
        if key not in self.hash:
            return -1
        
        # if key present then move node in end
        node = self.hash[key]
        # 1. if node is at head, then delete from head and insert at tail
        if node.prev == None:
            self.__deleteAtBeg()
            self.__insert(node.key, node.val)
        # 2. if node is at tail, do nothing and return value
        elif node.next == None:
            return node.val
        # 3. if node is in middle, then delete from middle and insert at tail
        else:
            self.__deleteInMiddle(node)
            self.__insert(node.key, node.val)
        
        # return value
        return node.val
    
    def put(self, key: int, value: int):    
        
        # if key to be inserted is already present, then move node to end
        if key in self.hash:
            node = self.hash[key]
            if node.prev == None:
                self.__deleteAtBeg()
                self.__insert(key, value)
            elif node.next == None:
                node.val = value
            else:
                self.__deleteInMiddle(node)
                self.__insert(key, value)
        # if key not present
        else:
            # if capacity is already full, then delete from beg and insert end
            if self.size == self.cap:
                self.__deleteAtBeg()
                self.__insert(key, value)
            # if there is space, then insert at end and increment size
            else:
                self.__insert(key, value)
                self.size += 1
   
# using OrderedDict 
from collections import OrderedDict
class LRUCache:
    
    def __init__(self, cap):
        self.cap = cap
        self.store = OrderedDict()
        
    def get(self, key: int) :
        if key not in self.store:
            return -1
        
        val = self.store[key]
        self.store.move_to_end(key)
        return val
 
    def put(self, key: int, value: int)  :  
        
        if key in self.store:
            self.store[key] = value
            self.store.move_to_end(key)
        else:
            self.store[key] = value
        
        if len(self.store) > self.cap:
            self.store.popitem(last=False)
        
   