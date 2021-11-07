# name : hossam hegly , id:315533570

# to implement lru-cache we need to find in o(1) and add an item in o(1) so inorder to find an item in o(1) we use
# a hashtable (dictionary) and iroeder to add or remove an item in o(1) we use a bidirectional linked list
# so we're basically implementin a hashtable with a cicular bidirictional linked list
# the least item we used is the  is the item previous to head and the most recent is after head

# node for linked list
class node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class lru_cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = node(0, 0)  # to pin point which item is the most recent and least used
        self.size = 0
        self.dict = dict()

    # function to add a node to the linked list

    def addnode(self, node):
        if self.size == 0:  # first item is the most recent and least item we used so its the previous item and the next item to head
            self.head.next = node
            self.size = self.size + 1
            self.head.prev = node
            node.prev = self.head
            node.next = self.head
            self.dict[node.key] = node


        elif self.size < self.capacity:  # add new node to the start of the list
            tmp = self.head.next
            self.head.next = node
            tmp.prev = node
            node.prev = self.head
            node.next = tmp
            self.size = self.size + 1
            self.dict[node.key] = node

        else:  # if size > capacity swap delete least used item (previous to head)  and add new node at the start(after  head)
            tmp = self.head.next
            self.head.next = node
            tmp.prev = node
            node.prev = self.head
            node.next = tmp
            self.dict[node.key] = node

            tmp2 = self.head.prev
            tmp2.prev.next = self.head
            self.head.prev = tmp2.prev
            self.dict.pop(tmp2.key)
            del tmp2

    # remove a node from the linked list
    def removenode(self, node):
        n = node.next
        p = node.prev
        node.prev.next = n
        node.next.prev = p
        self.size = self.size - 1

    # add an item to the cache
    def __setitem__(self, key, value):
        n = node(key, value)

        if key in self.dict:  # already exists just deleted the item and then add it to the front of the list after head
            tmp = self.dict[key]
            self.removenode(tmp)

            self.addnode(n)

        else:
            self.addnode(n)

    def __getitem__(self, key):
        if key not in self.dict:  # throw exceptio nif item isnt in the cache
            raise -1

        else:  # if item exists then we just deleted it from the list and add it the the front (after head(
            n = self.dict[key]

            self.removenode(n)
            self.addnode(n)
            return n.value

