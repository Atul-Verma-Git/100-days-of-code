class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict = {}
        for i,j in prerequisites:
            dict.setdefault(i,[])
            dict[i].append(j)
        for i in range(numCourses):
            dict.setdefault(i,[])
        
        visited = [0] * numCourses
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            
            for x in dict[node]:
                if not dfs(x):
                    return False
            visited[node] = 1
            return True
        
        return all(dfs(i) for i in range(numCourses))
            
            
                
            
        
            