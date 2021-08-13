class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        t = 1
        num = 1
        count = 1
        n = 12
        while n < neededApples:
            num = num + 2
            t = t + num
            count = count + 1
            n = n + (12 * t)
            
        return count * 8
        