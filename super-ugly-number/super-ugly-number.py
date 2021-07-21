'''
[1,2,7,13,19] count = 1
[1,2,7,13,19] count = 2 condition check if each calculted no < next prime (output[count+1])
[1, 2 , 4, 7 ,13,  19] count = 3 check 
[1, 2 ,4 , 7 , 8]
'''


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        l = [1]
        heapq.heapify(l)
        def push(num):
            for i in primes:
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
            
        
        
        
                
                
            
                
            
            
                
            
            
            
            