from typing import List


def findMinDiff(arr: List[int], M: int):
    sorted_arr = sorted(arr)
    ans = sorted_arr[M-1] - sorted_arr[0]
    i = 1
    while i+M-1<len(sorted_arr):
        ans = min(ans, sorted_arr[i+M-1]-sorted_arr[i])
        i+=1
    return ans
        

def test_findMinDiff():
    test_cases = [
        {
            "arr": [3, 4, 1, 9, 9],
            "M": 5, 
            "output": 8
        },
        {
            "arr": [3, 4, 1, 9, 9, 10],
            "M": 5, 
            "output": 7
        },
        {
            "arr": [1, 2, 3, 4, 5, 6, 7],
            "M": 5, 
            "output": 4
        },
        {
            "arr": [3, 4, 1, 9, 56, 7, 9, 12],
            "M": 5, 
            "output": 6
        }
    ]

    for tc in test_cases:
        got = findMinDiff(tc["arr"], tc["M"])
        assert got==tc["output"], f"arr={tc["arr"]}, M={tc["M"]}"