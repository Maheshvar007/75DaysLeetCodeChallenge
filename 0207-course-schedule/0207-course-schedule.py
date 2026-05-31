class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        vis = [0] * numCourses
        def dfs(u):
            if vis[u] == 1:
                return False
            if vis[u] == 2:
                return True
            vis[u] = 1
            for v in g[u]:
                if not dfs(v):
                    return False
            vis[u] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True