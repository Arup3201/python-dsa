
def moveNegativePositive(nums):
    negatives = 0
    for i, item in enumerate(nums):
        if item<0:
            nums[i], nums[negatives] = nums[negatives], nums[i]
            negatives+=1

    print(nums)

def test_moveNegativePositive():
    test_cases = [
        {
            "original": [-12, 11, -13, -5, 6, -7, 5, -3, -6],
            "nums": [-12, 11, -13, -5, 6, -7, 5, -3, -6], 
            "output": [-12, -13, -5, -7, -3, -6, 11, 6, 5]
        }
    ]

    for tc in test_cases:
        moveNegativePositive(tc["nums"])
        assert set(tc["nums"])==set(tc["output"]), tc["original"]