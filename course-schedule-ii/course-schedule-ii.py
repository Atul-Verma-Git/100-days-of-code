class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {}
        for i, j in prerequisites:
            d.setdefault(i,[])
            d[i].append(j)
        for i in range(numCourses):
            d.setdefault(i,[])
        
        visited = [0] * numCourses
        output = []
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            
            for x in d[node]:
                if not dfs(x):
                    return False
            visited[node] = 1
            output.append(node)
            return True
            
        if all(dfs(i) for i in range(numCourses)):
            return output
        return []
        
        
            
        
            
        