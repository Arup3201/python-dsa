from typing import List

def maxProfit(prices: List[int]) -> int:
    result = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        result = max(result, prices[i]-buy)
        
        if buy>prices[i]:
            buy = prices[i]
        
    return result

def test_maxProfit():
    test_cases = [
        {
            "prices": [7,1,5,3,6,4], 
            "output": 5
        },
        {
            "prices": [7,6,4,3,1], 
            "output": 0
        },
    ]

    for tc in test_cases:
        got = maxProfit(tc["prices"])
        assert got==tc["output"], tc["prices"]