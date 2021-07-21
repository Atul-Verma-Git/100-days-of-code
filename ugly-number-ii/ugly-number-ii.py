class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        l = [1]
        heapq.heapify(l)
        def push(num):
            for i in [2,3,5]:
                heapq.heappush(l,num*i)
        count = 0
        m = 0
        while count <= n:
            t = heapq.heappop(l)
            if m!= t:
                count += 1
                push(t)
                m = t
            if count == n:
                return t
            
        
        