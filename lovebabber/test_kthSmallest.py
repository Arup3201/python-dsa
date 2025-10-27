from typing import List
import heapq

def kthSmallest(arr: List[int], k: int) -> int:
    pq = []

    for item in arr:
        heapq.heappush(pq, -item)

        if len(pq) > k:
            heapq.heappop(pq)

    return -pq[0]

def test_kthSmallest():
    test_cases = [
        {
            "arr": [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 
            "k": 4, 
            "output": 5
        },
        {
            "arr": [7, 10, 4, 3, 20, 15], 
            "k": 3, 
            "output": 7
        },
    ]

    for tc in test_cases:
        got = kthSmallest(tc["arr"], tc["k"])
        assert got==tc["output"], tc["arr"]