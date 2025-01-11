from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {idx:[] for idx in range(numCourses)}

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        seen = set()
        current = set()
        res = []

        def dfs(start):
            if start in current:
                return True
            if start in seen:
                return False
            
            current.add(start)

            for neighbor in adj[start]:
                if dfs(neighbor):
                    return True
            
            current.remove(start)
            seen.add(start)
            res.append(start)
            
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []

        return res[::-1]


        

