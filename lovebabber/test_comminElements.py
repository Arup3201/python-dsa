from typing import List

def commonElements(arr1: List[int], arr2: List[int], arr3: List[int]):
    i, j, k = 0, 0, 0
    common = []
    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])

            i+=1
            j+=1
            k+=1

            while i<len(arr1) and arr1[i]==arr1[i-1]:
                i+=1
            while j<len(arr2) and arr2[j]==arr2[j-1]:
                j+=1
            while k<len(arr3) and arr3[k]==arr3[k-1]:
                k+=1

        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1

    if len(common)==0:
        return [-1]

    return common

def test_commonElements():
    test_cases = [
        {
            "arr1": [1, 5, 10, 20, 40, 80], 
            "arr2": [6, 7, 20, 80, 100], 
            "arr3": [3, 4, 15, 20, 30, 70, 80, 120], 
            "output": [20, 80]
        },
        {
            "arr1": [1, 2, 3, 4, 5], 
            "arr2": [6, 7], 
            "arr3": [8,9,10], 
            "output": [-1]
        },
        {
            "arr1": [1, 1, 1, 2, 2, 2], 
            "arr2": [1, 1, 2, 2, 2], 
            "arr3": [1, 1, 1, 1, 2, 2, 2, 2], 
            "output": [1, 2]
        },
        {
            "arr1": [11, 13, 14, 45, 62, 72, 79, 90], 
            "arr2": [13, 24, 27, 31, 62, 74, 89, 89, 96], 
            "arr3": [12, 48, 58, 60, 62, 65, 88], 
            "output": [62]
        },
    ]

    for tc in test_cases:
        got = commonElements(tc["arr1"], tc["arr2"], tc["arr3"])
        assert got==tc["output"], f"arr1={tc["arr1"]}, arr2={tc["arr2"]}, arr3={tc["arr3"]}"