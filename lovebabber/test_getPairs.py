from typing import List

def getPairs(arr: List[int]):
    pairs = []
    negatives = dict()
    for item in arr:
        if item<0:
            if not negatives.get(item, False):
                negatives[item] = True
    
    for item in arr:
        if item>0:
            if negatives.get(-item, False):
                pairs.append([-item, item])
                negatives[-item] = False

    cnt = 0
    for item in arr:
        if item==0:
            cnt+=1
    if cnt>1:
        pairs.append([0, 0])

    pairs.sort(key=lambda x: x[0])
    return pairs


def test_getPairs():
    test_cases = [
        {
            "arr": [-1, 0, 1, 2, -1, -4],
            "output": [[-1, 1]]
        }, 
        {
            "arr": [-1, 0, 1, 0, 2, -1, -4],
            "output": [[-1, 1], [0, 0]]
        }, 
        {
            "arr": [6, 1, 8, 0, 4, 0, -9, -1, -10, -6, -5],
            "output": [[-6, 6],[-1, 1], [0, 0]]
        }, 
        {
            "arr": [6, 1, 8],
            "output": []
        }, 
        {
            "arr": [6, -6, 8, -8],
            "output": [[-8, 8], [-6, 6]]
        }, 
    ]
    for tc in test_cases:
        got = getPairs(tc["arr"])
        assert got==tc["output"], tc["arr"]