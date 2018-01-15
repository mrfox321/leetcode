class dNode(object):

    def __init__(self,key,val):

        self.key = key
        self.val = val
        self.front = None
        self.back = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}
        self.cap = capacity
        self.head = None
        self.end = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table:
            return -1

        self.reorder(key)
        return self.table[key].val



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.table:
            node = dNode(key,value)

            if not self.table and self.cap > 0: #empty cache
                self.head = node
                self.end = node
                self.table[key] = node

            elif len(self.table) < self.cap: #available capacity
                self.head.front = node
                node.back = self.head
                self.head = node
                self.table[key] = node

            else:  #cache is full
                self.head.front = node
                node.back = self.head
                self.head = node
                self.table[key] = node
                #change end
                end_node = self.end
                self.end = end_node.front
                self.end.back = None
                #remove element from dict
                self.table.pop(end_node.key,None)


        else:
            self.reorder(key)
            self.table[key].val = value

    def reorder(self,key):

        node = self.table[key]

        if node is self.head: #already at front of list
            return
        elif node is self.end and node.front is not None: #checking node.next ensures it is not a single element cache
            self.end = node.front
            self.end.back = None
            node.front = None
            self.head.front = node
            node.back = self.head
            self.head = node
            return

        else: #node is in middle of cache
            back_node = node.back
            front_node = node.front
            back_node.front = front_node
            front_node.back = back_node
            node.front = None
            node.back = self.head
            self.head.front = node
            self.head = node
            return
