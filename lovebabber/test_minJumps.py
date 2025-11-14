memo = [-2]*(10**5+1)
def minJumpsRec(i, arr):
    if memo[i] != -2:
        return memo[i]
    
    n = len(arr)
    if arr[i]<=0:
        memo[i] = -1
    if i==n-2 or i+arr[i]>=n-1:
        memo[i] = 1
    else:
        memo[i] = -1
        for j in range(i+1, min(n-1, i+arr[i]+1)):
            memo[j] = minJumpsRec(j, arr)
            if memo[i]==-1 and memo[j]!=-1:
                memo[i] = 1+memo[j]
            elif memo[j]!=-1:
                memo[i] = min(memo[i], 1+memo[j])
    return memo[i]

def minJumps(arr):
    # code here
    global memo 
    memo = [-2]*(10**5+1)
    return minJumpsRec(0, arr)

def test_minJumps():
    test_cases = [
        {
            "arr": [2, 5], 
            "output": 1
        },
        {
            "arr": [1, 3, 5], 
            "output": 2
        }, 
        {
            "arr": [1, 3, 5, 8], 
            "output": 2
        }, 
        {
            "arr": [1, 1, 0, 2], 
            "output": -1
        }, 
        {
            "arr": [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 
            "output": 3
        }
    ]

    for tc in test_cases:
        got = minJumps(tc["arr"])
        assert got==tc["output"], tc["arr"]

if __name__=="__main__":
    arr = [1, 2, 0, 0, 0]
    print(minJumps(arr))