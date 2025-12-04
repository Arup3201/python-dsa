def dfs(adj):
    st = []
    result = []
    V = len(adj)
    visited = [False]*V
    
    st.append(0)
    
    while len(st)>0:
        n = st.pop()
        
        if visited[n]:
            continue
        
        visited[n] = True
        result.append(n)
        
        size = len(adj[n])
        for i in range(size-1, -1, -1):
            v = adj[n][i]
            if not visited[v]:
                st.append(v)
                
    return result