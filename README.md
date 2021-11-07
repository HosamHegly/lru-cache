### **lru_cache class implementation**

### **Explination:**
lru_cache is a cache with a fixed size that the user defines and when ever we want to enter a value in the cache when its full we remove the least item we used and add the value we want to add as the most recent item we used and also when we want to return a value then this value is now the most recent item we used

### **implemination:**
**class node:**
this class is for implementing the circular linked list it has previous node, next node, key and value 

**class lru_cache:**
i used a dictionary that contains nodes of a circular bidirectional linked list. the dictionary allows us to get the value of a key in o(1) and the linked list allows us to add/remove in order of input in o(1). to add values we add values to the linked list in order of entrance and when the cache is full we add the key value to the start of the linked list and remove the value at the end of the linked list after head ( a tag node that tells us which is the first node and which is the last). and when we want to return a value then we remove its node and add it to the start of the linked list ( after the head node)

### **required:**
python

### examples:
cache = lru_cache(2)

cache[1] = 1 # cache is {1=1}

cache[2] = 2 # cache is {1=1, 2=2}

cache[1] # return 1

cache[3] = 3 # LRU key was 2, evicts key 2, cache is {1=1, 3=3}

cache[2] # Throws an exception (not found)

cache[4] = 4 # LRU key was 1, evicts key 1, cache is {4=4, 3=3}

cache[1] # Throws an exception (not found)

cache[4] # return 4

cache[3] # return 3

cache[5] = 5 # LRU key was 4, evicts key 4, cache is {3=3, 5=5}

cache[4] # Throws an exception (not found)

cache[3] # return 3

cache[5] # return 5

### **how to run:**
clone and run lru_cache,py




