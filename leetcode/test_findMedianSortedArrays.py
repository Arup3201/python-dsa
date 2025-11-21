from typing import List

def findMedianSortedArrays(num1: List[int], num2: List[int]):
    m = len(num1)
    n = len(num2)
    
    l1, r1 = 0, m-1
    l2, r2 = 0, n-1
    while l1<=r1 and l2<=r2:
        mid1 = l1 + (r1-l1)//2
        mid2 = l2 + (r2-l2)//2
        if num1[mid1]<num2[mid2] and num1[mid1-1]<num2[mid2+1]:
            if m+n%2==0:
                return num1[mid1]+num2[mid2] // 2
            else:
                return num1[mid1+1]



def test_findMedianSortedArrays():
    test_cases = [
        {
            "num1": [1, 2, 3], 
            "num2": [5, 6], 
            "output": 3
        }
    ]

    for tc in test_cases:
        got = findMedianSortedArrays(tc["num1"], tc["num2"])
        assert got==tc["output"], f"num1={tc["num1"]}, num2={tc["num2"]}"