class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        d = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        l = [[-val,key] for key,val in d.items()]
        heapq.heapify(l)
        
        output = ""
        while len(l)>1:
            count1, char1 = heapq.heappop(l)
            count2, char2 = heapq.heappop(l)
            output += char1+char2
            
            if -count1 > 1:
                heapq.heappush(l,[count1+1, char1])
            if -count2 > 1:
                heapq.heappush(l,[count2+1, char2])
        if l:
            count , char = heapq.heappop(l)
            if -count > 1:
                return ""
            return output+char
        return output
            
        
            
                
        