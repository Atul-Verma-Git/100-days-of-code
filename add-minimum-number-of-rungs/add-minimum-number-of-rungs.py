class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        temp = 0
        count = 0
        
        for i in range(len(rungs)):
            if rungs[i] - temp <= dist:
                temp = rungs[i]
                
            else:
                if (rungs[i] - temp) % dist == 0:
                    count = count + ((rungs[i] - temp) // dist) - 1
                else:
                    count = count + ((rungs[i] - temp) // dist) 
                temp = rungs[i]
        return count
            
        