class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        

    def add(self, key: int) -> None:
        if key not in self.h.keys():
            self.h[key] = key
        
        

    def remove(self, key: int) -> None:
        if key in self.h.keys():
            del self.h[key]
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.h.keys():
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)