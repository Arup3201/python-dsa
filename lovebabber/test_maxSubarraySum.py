from typing import List

def maxSubarraySum(arr: List[int]):
    ans = arr[0]
    curr = arr[0]
    i = 1
    while i<len(arr):
        curr = max(curr+arr[i], arr[i])
        ans = max(ans, curr)
        i+=1

    return ans

def test_maxSubarraySum():
    test_cases = [
        {
            "arr": [2, 3, -8, 7, -1, 2, 3], 
            "output": 11
        },
        {
            "arr": [-2, -4], 
            "output": -2
        },
        {
            "arr": [5, 4, 1, 7, 8], 
            "output": 25
        },
    ]

    for tc in test_cases:
        got = maxSubarraySum(tc["arr"])
        assert got==tc["output"], tc["arr"]