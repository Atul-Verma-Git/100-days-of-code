class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        b = nums[:k]
        heapq.heapify(b)
        for i in range(k,len(nums)):
            if b[0] < nums[i]:
                heapq.heapreplace(b, nums[i])
        return b[0]
        
        