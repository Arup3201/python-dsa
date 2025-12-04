import sys, heapq

def dijkstra(V, edges, src):
    adj = [[] for _ in range(V)]
    for edge in edges:
        adj[edge[0]].append((edge[1], edge[2]))
        adj[edge[1]].append((edge[0], edge[2]))
    
    finalized = [False]*V
    dist = [sys.maxsize]*V
    
    dist[src] = 0
    
    pq = []
    for i, d in enumerate(dist):
        heapq.heappush(pq, [d, i])
    
    while len(pq)>0:
        _, u = heapq.heappop(pq)
        if finalized[u]:
            continue
        
        finalized[u] = True
        
        for v, w in adj[u]:
            if not finalized[v] and dist[v]>dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, [dist[v], v])
    
    return dist