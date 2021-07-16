"""
5425161436
5 top = 5, minv = 5,
54 top = 4, minv = 4
542 top = 2 minv = 2
5425 top = 5 minv =2
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.MinE = None
            
    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.minE = val
        
        else:
            if val >= self.minE:
                self.stack.append(val)

            else:
                self.stack.append(2 * val - self.minE)
                self.minE = val

    def pop(self) -> None:
        y = self.stack[-1]
        if y >= self.minE:
            del self.stack[-1]
    
        else:
            del self.stack[-1]
            self.minE = 2 * self.minE - y


    def top(self) -> int:
        y = self.stack[-1]
        if y >= self.minE:
            return y
        else:
            return self.minE
        

    def getMin(self) -> int:
        return self.minE
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()