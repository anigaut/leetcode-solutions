'''
- Not exactly a linked list problem, although a doubly-linked list can be used
- Remember that a hashmap is ordered - the keys are stored in the order they are added
- Each time the 'get' operation is run for a key, it becomes the most-recently used
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
    
    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)

        if val != -1:
            del self.cache[key]
            self.cache[key] = val

        return val

    def put(self, key: int, value: int) -> None:
        cur_val = self.cache.get(key, -1)

        if cur_val == -1:
            if len(self.cache) == self.capacity:
                LRU_key = list(self.cache.keys())[0]
                del self.cache[LRU_key]
        else:
            del self.cache[key]

        self.cache[key] = value 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)