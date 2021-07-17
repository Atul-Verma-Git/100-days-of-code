class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(i, j):
            return (j -i) * min(height[i], height[j])

        i = 0
        j = len(height) - 1
        a = 0
        while i != j:
            if height[j] > height[i]:
                temp = area(i, j)
                i += 1
            else:
                temp = area(i,j)
                j -= 1
            a = max(a, temp)
            
            
        return a
            
            
            
        
        