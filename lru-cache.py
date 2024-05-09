class ListNode:
    def __init__(self, key, val, next=None, prev = None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):

        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._remove_node(n)
            self._add_head(n)
            return n.val
        else:
            return -1

    def _add_head(self, n: ListNode):
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n
    
    def _remove_node(self, n: ListNode):
        n.prev.next = n.next
        n.next.prev = n.prev

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            n = self.d[key]
            del self.d[key]
            self._remove_node(n)
        
        if len(self.d) == self.capacity:
            n = self.d[self.tail.prev.key]
            del self.d[n.key]
            self._remove_node(n)
        
        n = ListNode(key, value)
        self._add_head(n)
        self.d[key] = n

        


        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.put(3,3))
print(obj.get(2))
print(obj.put(4,4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

