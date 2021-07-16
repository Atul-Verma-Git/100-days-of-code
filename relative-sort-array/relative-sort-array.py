class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i in arr1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        output = []
        for i in arr2:
            output += [i] * d[i]
            count = d[i]
            while count > 0:
                arr1.remove(i)
                count -= 1
        arr1.sort()
        return output+arr1
        
            
            
        