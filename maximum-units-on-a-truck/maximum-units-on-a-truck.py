class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda x: x[1])
        count =  0
        output = 0
        for i in range(len(boxTypes)):
            if truckSize - count >= boxTypes[i][0]:
                output += boxTypes[i][1] * boxTypes[i][0]
                count += boxTypes[i][0]
            else:
                output += boxTypes[i][1] * (truckSize - count)
                count = 0
            if count == 0:
                return output
        return output
            
            
        