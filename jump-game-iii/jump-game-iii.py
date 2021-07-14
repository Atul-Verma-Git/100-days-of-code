class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        myqueue = []
        visited = [False] * len(arr)
        myqueue.append(start)
        
        while myqueue != []:
            i = myqueue[0]
            if arr[i] == 0:
                return True
            del myqueue[0]
            visited[i] = True
            if i + arr[i] < len(arr):
                if arr[i + arr[i]] == 0  and visited[i + arr[i]] == False:
                    return True
                if visited[i + arr[i]] == False:
                    myqueue.append(i + arr[i])
            if i - arr[i] >= 0 :
                if arr[i - arr[i]] == 0 and visited[i - arr[i]] == False:
                    return True
                if visited[i - arr[i]] == False:
                    myqueue.append(i - arr[i])
        return False
            
            
            