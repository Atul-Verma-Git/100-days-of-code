

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        def get_max(myheap,start):
            while True:
                num, index = myheap[0]
                if index >= start:
                    return -num
                heapq.heappop(myheap)
                
        output = []
        myheap = [[-nums[i],i] for i in range(k-1)]
        heapq.heapify(myheap)
        for i,j in enumerate(nums[k-1:],k-1):
            heapq.heappush(myheap,[-j,i])
            output.append(get_max(myheap,i-k+1))
        return output
    