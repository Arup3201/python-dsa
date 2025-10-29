from typing import List

def nextPermutation(nums: List[int]) -> None:
    index = -1
    for i in range(len(nums)-2, -1, -1):
        if nums[i]<nums[i+1]:
            index = i
            break
    
    if index == -1:
        reverse(nums, 0, len(nums)-1)
        return
    
    larger = -1
    for i in range(len(nums)-1, index, -1):
        if nums[i] > nums[index]:
            larger = i
            break
    
    nums[index], nums[larger] = nums[larger], nums[index]
    reverse(nums, index+1, len(nums)-1)


def reverse(nums: List[int], low: int, high: int):
    while low<high:
        nums[low], nums[high] = nums[high], nums[low]

        low+=1
        high-=1

def test_nextPermutation():
    test_cases = [
        {
            "original": [1, 2, 3], 
            "nums": [1, 2, 3], 
            "output": [1, 3, 2]
        },
        {
            "original": [1, 1, 5], 
            "nums": [1, 1, 5], 
            "output": [1, 5, 1]
        },
        {
            "original": [3, 2, 1], 
            "nums": [3, 2, 1], 
            "output": [1, 2, 3]
        },
        {
            "original": [2, 3, 4, 1], 
            "nums": [2, 3, 4, 1], 
            "output": [2, 4, 1, 3]
        },
        {
            "original": [2, 4, 3, 1], 
            "nums": [2, 4, 3, 1], 
            "output": [3, 1, 2, 4]
        },
        {
            "original": [1], 
            "nums": [1], 
            "output": [1]
        },
    ]

    for tc in test_cases:
        nextPermutation(tc["nums"])
        assert tc["nums"]==tc["output"], tc["original"]