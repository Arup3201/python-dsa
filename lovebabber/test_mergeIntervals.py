from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(intervals)):
        if intervals[index][1] >= intervals[i][0]:
            intervals[index][1] = max(intervals[index][1], intervals[i][1])
        else:
            index+=1
            intervals[index] = intervals[i]

    return intervals[:index+1]

def test_merge():
    test_cases = [
        {
            "intervals": [[1,3],[2,6],[8,10],[15,18]], 
            "output": [[1,6],[8,10],[15,18]]
        }, 
        {
            "intervals": [[1,4],[4,5]], 
            "output": [[1,5]]
        }, 
        {
            "intervals": [[4,7],[1,4]], 
            "output": [[1,7]]
        }
    ]

    for tc in test_cases:
        got = merge(tc["intervals"])
        assert got == tc["output"], tc["intervals"]