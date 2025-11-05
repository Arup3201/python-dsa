def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()

    res = arr[n-1] - arr[0]

    for i in range(1, n-1):
        if arr[i] - k < 0:
            continue

        minH = min(arr[0]+k, arr[i]-k)
        maxH = max(arr[i-1]+k, arr[n-1]-k)
        
        res = min(res, maxH-minH)

    return res

def test_getMinDiff():
    test_cases = [
        {
            "arr": [5, 8, 1, 10],
            "k": 2,
            "output": 5
        }, 
        {
            "arr": [3, 9, 12, 16, 20],
            "k": 3,
            "output": 11
        }, 
    ]
    for tc in test_cases:
        got = getMinDiff(tc["arr"], tc["k"])
        assert got==tc["output"], tc["arr"]