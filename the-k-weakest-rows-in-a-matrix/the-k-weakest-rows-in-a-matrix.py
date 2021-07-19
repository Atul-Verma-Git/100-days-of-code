class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import heapq
        arr = [[sum(n),i] for i,n in enumerate(mat)]
        heapq.heapify(arr)
        output = []
        for i in range(k):
            num, i = heapq.heappop(arr)
            output.append(i)
        return output
        
        