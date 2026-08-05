class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        vis=[False]*n
        for u, v in invocations:
            adj[u].append(v)
        def dfs(u):
            vis[u]=True
            for v in adj[u]:
                if vis[v]: continue
                dfs(v)
        dfs(k)
        cnnt1=False
        for u, v in invocations:
            if not vis[u] and vis[v]:
                cnnt1=True
                break
        if cnnt1:
            return list(range(n))
        return [i for i in range(n) if not vis[i]]
        