import sys

def spanningTree(V, edges):
    # code here
    adj = [[] for _ in range(V)]
    for edge in edges:
        adj[edge[0]].append((edge[1], edge[2]))
        adj[edge[1]].append((edge[0], edge[2]))
    
    keys = [sys.maxsize]*V
    finalized = [False]*V
    weight = 0
    
    keys[0] = 0
    
    for _ in range(V):
        u = -1
        for i in range(V):
            if not finalized[i] and (u==-1 or keys[i]<keys[u]):
                u = i
                
        finalized[u] = True
        weight += keys[u]
        
        for v, w in adj[u]:
            if not finalized[v]:
                keys[v] = min(keys[v], w)
                
    return weight