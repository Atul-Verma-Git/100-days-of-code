class CustomStack:

    def __init__(self, maxSize: int):
        self.m = maxSize
        self.stack = []
        self.l = 0

    def push(self, x: int) -> None:
        if self.l < self.m:
            self.stack.append(x)
            self.l += 1

    def pop(self) -> int:
        if self.stack == []:
            return -1
        self.l -= 1
        return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        t = 0
        if k < self.l:
            t = k
        else:
            t = self.l
        for i in range(t):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)