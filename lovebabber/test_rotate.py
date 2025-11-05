def reverse(arr, low, high):
    while low<high:
        arr[low], arr[high] = arr[high], arr[low]
        low+=1
        high-=1

def rotate(arr):
    n = len(arr)
    reverse(arr, 0, n-2)
    reverse(arr, 0, n-1)

def test_rotate():
    test_cases = [
        {
            "original": [1, 2, 3, 4, 5],
            "arr": [1, 2, 3, 4, 5],
            "output": [5, 1, 2, 3, 4]
        }, 
        {
            "original": [9, 8, 7, 6, 4, 2, 1, 3],
            "arr": [9, 8, 7, 6, 4, 2, 1, 3],
            "output": [3, 9, 8, 7, 6, 4, 2, 1]
        }, 
    ]

    for tc in test_cases:
        rotate(tc["arr"])
        assert tc["arr"]==tc["output"], tc["original"]