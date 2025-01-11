from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {idx:[] for idx in range(numCourses)}

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        seen = set()
        visiting = set()

        def dfs(start):
            if start in visiting:
                return True
            if start in seen:
                return False

            visiting.add(start)
        
            for neighbor in adj[start]:
                if dfs(neighbor):
                    return True

            seen.add(start)
            visiting.remove(start)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True