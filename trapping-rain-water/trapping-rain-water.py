class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        a = [0]
        i = 0
        while i < len(height):
            if height[i] >= a[0]:
                a = [height[i]]
                i += 1
            else:
                break
        m = a[0]
        while i < len(height):
            if height[i] <= a[-1]:
                a.append(height[i])
                i += 1
            elif height[i] >= m:
                for j in a:
                    output += (m-j)
                a = [height[i]]
                m = a[0]
                i += 1
            else:
                j = len(a) - 1
                while a[j] < height[i]:
                    output += (height[i] - a[j])
                    a[j] = height[i]
                    j -= 1
                    
        return output
            
                
            
                