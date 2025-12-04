from collections import deque

def topoSort(self, V, edges):
    indeg = [0]*V
    adj = [[] for _ in range(V)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        indeg[edge[1]]+=1
        
    q = deque()
    for i, d in enumerate(indeg):
        if d==0:
            q.append(i)
            
    result = []
    while len(q)>0:
        u = q.popleft()
        result.append(u)
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v]==0:
                q.append(v)
                
    return result