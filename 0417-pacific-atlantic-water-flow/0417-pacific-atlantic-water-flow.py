class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, vis):
            vis.add((r, c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in vis and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, vis)
        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n - 1, atl)
        for c in range(n):
            dfs(0, c, pac)
            dfs(m - 1, c, atl)
        return list(pac & atl)