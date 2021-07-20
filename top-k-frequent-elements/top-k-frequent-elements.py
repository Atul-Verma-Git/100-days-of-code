class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        l = [[-val,key] for key,val in d.items()]
        heapq.heapify(l)
        output = []
        i = 0
        while i < k:
            b = heapq.heappop(l)
            output.append(b[1])
            i += 1
        return output