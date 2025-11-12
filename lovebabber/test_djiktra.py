from dataclasses import dataclass, field
from typing import Any
import heapq

@dataclass(order=True)
class PriorityItem:
    priority: int
    index: Any = field(compare=False)

def dijkstra(V, edges, src):
    # code here
    adj = [[] for _ in range(V)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2]])
        adj[edge[1]].append([edge[0], edge[2]])

    visited = [False]*V
    dist = [10**9]*V

    dist[src] = 0

    pq = []
    for i, d in enumerate(dist):
        heapq.heappush(pq, PriorityItem(d, i))

    for _ in range(V):
        t = heapq.heappop(pq)
        u = t.index

        visited[u] = True
        for v, w in adj[u]:
            if not visited[v] and dist[v]>dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, PriorityItem(dist[v], v))

    return dist

def test_dijkstra():
    test_cases = [
        {
            "V": 3,
            "edges": [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 
            "src": 2, 
            "output": [4, 3, 0]
        }
    ]

    for tc in test_cases:
        dist = dijkstra(tc["V"], tc["edges"], tc["src"])
        assert dist==tc["output"], f"edges={tc["edges"]}, src={tc["src"]}"