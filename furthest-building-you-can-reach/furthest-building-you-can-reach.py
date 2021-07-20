class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq
        count = 1
        i = 1
        l = []
        heapq.heapify(l)
        while i < len(heights):
            if heights[i] <= heights[i-1]:
                count += 1
                i += 1
            else:
                if heights[i] - heights[i-1] <= bricks:
                    heapq.heappush(l, -(heights[i] - heights[i-1]))
                    bricks -= (heights[i] - heights[i-1])
                    count += 1
                    i += 1
                else:
                    if ladders > 0: 
                        if len(l)> 0:
                            x = heapq.heappop(l)
                            if -x < (heights[i] - heights[i-1]):
                                heapq.heappush(l,x)
                            else:
                                bricks += -x
                                i -= 1
                        ladders -= 1
                        i += 1
                        
                    else:
                        return i-1
        return i-1
                
            
        