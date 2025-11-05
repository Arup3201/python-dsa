def countOccurence(arr, k):
    n = len(arr)
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    
    cnt=0
    for it, fr in freq.items():
        if fr > n/k:
            cnt+=1

    return cnt

def test_countOccurence():
    test_cases = [
        {
            "arr": [3, 1, 2, 2, 1, 2, 3, 3],
            "k": 4,
            "output": 2
        }, 
         {
            "arr": [2, 3, 3, 2],
            "k": 3,
            "output": 2
        }, 
    ]

    for tc in test_cases:
        got = countOccurence(tc["arr"], tc["k"])
        assert got==tc["output"], tc["arr"]