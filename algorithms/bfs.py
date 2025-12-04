def bfs(adj):
    V = len(adj)
    q = []
    visited = [False]*V
    
    visited[0] = True
    q.append(0)
    
    res = []
    
    while len(q)>0:
        u = q.pop(0)
        res.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                
    return res