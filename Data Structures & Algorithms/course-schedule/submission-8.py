class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        
        for pr in prerequisites:
            prereq[pr[0]].append(pr[1])
        
        def dfs(i):
            if i in visited:
                return False
            
            if len(prereq[i]) == 0:
                return True
            
            res = True
            visited.add(i)
            for ele in prereq[i]:
                res = res and dfs(ele)
            if res:
                prereq[i] = []
            visited.remove(i)
            return res
        
        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
        return True
                
