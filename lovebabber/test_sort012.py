from typing import List

def sort012(arr: List[int]):
    low, mid, high = 0, 0, len(arr)-1
    while mid<=high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low+=1
            mid+=1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
        else:
            mid+=1

def test_sort012():
    test_cases = [
        {
            "original": [0, 1, 2, 0, 1, 2], 
            "arr": [0, 1, 2, 0, 1, 2], 
            "output": [0, 0, 1, 1, 2, 2]
        },
        {
            "original": [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1], 
            "arr": [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1], 
            "output": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
        },
    ]

    for tc in test_cases:
        sort012(tc["arr"])
        assert tc["arr"]==tc["output"], tc["original"]