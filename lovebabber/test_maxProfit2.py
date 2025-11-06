
def maxProfit(prices):
    # code here
    n = len(prices)
    profits = [0]*n
    
    sell = prices[n-1]
    for i in range(n-2, 0, -1):
        sell = max(sell, prices[i])
        
        profits[i] = max(profits[i+1], sell-prices[i])
    
    res = 0
    buy = prices[0]
    for i in range(1, n):
        buy = min(buy, prices[i])
        
        res = max(res, profits[i]+(prices[i]-buy))
        
    return res

def test_maxProfit():
    test_cases = [
        {
            "prices": [10, 22, 5, 75, 65, 80], 
            "output": 87
        },
        {
            "prices": [2, 30, 15, 10, 8, 25, 80], 
            "output": 100
        },
    ]

    for tc in test_cases:
        got = maxProfit(tc["prices"])
        assert got==tc["output"], tc["prices"]