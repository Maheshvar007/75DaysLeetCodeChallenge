class Solution(object):
    def findWords(self, board, words):
        trie = {}
        for w in words:
            cur = trie
            for c in w:
                cur = cur.setdefault(c,{})
            cur['#'] = w
        m,n = len(board),len(board[0])
        ans=[]
        def dfs(i,j,node):
            c=board[i][j]
            if c not in node:
                return
            nxt=node[c]
            if '#' in nxt:
                ans.append(nxt['#'])
                del nxt['#']
            board[i][j]='*'
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj=x+i,y+j
                if (0<=ni<m and 0<=nj<n and
                    board[ni][nj] != '*'):
                    dfs(ni,nj,nxt)
            board[i][j]=c
        for i in range(m):
            for j in range(n):
                dfs(i,j,trie)
        return ans