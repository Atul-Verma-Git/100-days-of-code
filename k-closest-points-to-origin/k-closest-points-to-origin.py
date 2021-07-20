class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        arr = []
        for i in points:
            d = i[0]**2 +i[1]**2
            arr.append([d,i])
            
        heapq.heapify(arr)
        i = 0
        output = []
        while i < k:
            b = heapq.heappop(arr)
            output.append(b[1])
            i += 1
        return output
            
            
        