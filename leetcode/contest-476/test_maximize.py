from typing import List

def maximizeExpressionOfThree(nums: List[int]) -> int:
    ai = 0
    bi = 1
    if nums[ai]<nums[bi]:
        ai, bi = bi, ai

    n = len(nums)
    for i in range(2, n):
        if nums[ai]<nums[i]:
            bi = ai
            ai = i
        elif nums[bi]<nums[i]:
            bi = i
    print(nums[ai], nums[bi], min(nums))
    return nums[ai]+nums[bi]-min(nums)

def test_maximizeExpressionOfThree():
    test_cases = [
        {
            "arr": [1,4,2,5], 
            "output": 8
        }
    ]

    for tc in test_cases:
        got = maximizeExpressionOfThree(tc["arr"])
        assert got==tc["output"], tc["arr"]
