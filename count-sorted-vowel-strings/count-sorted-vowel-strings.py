"""
1-> 1, 1, 1, 1, 1 
2-> 5, 4 ,3 , 2 , 1
3-> 15, 10 , 6 ,3 ,1
4-> 
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        now = [1] * 5
        for i in range(1,n):
            next = [sum(now[_:5]) for _ in range(5)]
            now = next
        return sum(now)
            
            
        