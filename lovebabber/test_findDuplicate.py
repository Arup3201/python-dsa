from typing import List

def findDuplicate(nums: List[int]) -> int:
    low, high = 1, len(nums)-1

    while low<high:
        mid = low + (high-low) // 2

        cnt = 0
        for i in range(len(nums)):
            if nums[i]<=mid:
                cnt += 1
        
        if cnt<=mid:
            low = mid+1
        else:
            high=mid

    return low

def test_findDuplicate():
    test_cases = [
        {
            "nums": [1,3,4,2,2], 
            "output": 2
        }, 
        {
            "nums": [3,1,3,4,2], 
            "output": 3
        }, 
        {
            "nums": [3, 3, 3, 3], 
            "output": 3
        }, 
        {
            "nums": [1, 3, 3, 3], 
            "output": 3
        }, 
        {
            "nums": [3, 2, 2], 
            "output": 2
        }
    ]

    for tc in test_cases:
        got = findDuplicate(tc["nums"])
        assert got==tc["output"], tc["nums"]