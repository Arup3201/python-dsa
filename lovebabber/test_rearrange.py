from typing import List

def rearrange(arr: List[int]):
    positives, negatives = [], []
    for item in arr:
        if item<0:
            negatives.append(item)
        else:
            positives.append(item)

    i, j, k = 0, 0, 0
    while k<len(arr):
        if k%2==0 and i<len(positives):
            arr[k] = positives[i]
            i+=1
        elif k%2!=0 and j<len(negatives):
            arr[k] = negatives[j]
            j+=1
        elif i<len(positives):
            arr[k] = positives[i]
            i+=1
        elif j<len(negatives):
            arr[k] = negatives[j]
            j+=1
        k+=1

def test_rearrange():
    test_cases = [
        {
            "original": [9, 4, -2, -1, 5, 0, -5, -3, 2],
            "arr": [9, 4, -2, -1, 5, 0, -5, -3, 2],
            "output": [9, -2, 4, -1, 5, -5, 0, -3, 2]
        }, 
        {
            "original": [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8],
            "arr": [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8],
            "output": [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
        }, 
    ]

    for tc in test_cases:
        rearrange(tc["arr"])
        assert tc["arr"]==tc["output"], tc["original"]