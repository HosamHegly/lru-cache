### lru_cache class implementation

### Explination:
lru_cache is a cache with a fixed size that the user defines and when ever we want to enter a value in the cache when its full we remove the least item we used and add the value we want to add as the most recent item we used and also when we want to return a value then this value is now the most recent item we used

**implemination:**
i used a dictionary that contains nodes of a circular bidirectional linked list. the dictionary allows us to get the value of a key in o(1) and the linked list allows us to add/remove in order of input in o(1) 

