from typing import List

result = []

def genParenthesis(n:int, open: int, close: int, output: str):
    if close==n:
        result.append(output)
        return

    if open<n:
        genParenthesis(n, open+1, close, output+"(")
    if close<open:
        genParenthesis(n, open, close+1, output+")")

def generateParenthesis(n: int) -> List[str]:
    result.clear()
    genParenthesis(n, 0, 0, "")
    return result

def test_generate():
    test_cases = [
        {
            "n": 1, 
            "output": ["()"]
        }, 
        {
            "n": 3, 
            "output": ["((()))","(()())","(())()","()(())","()()()"]
        },
    ]

    for tc in test_cases:
        got = generateParenthesis(tc["n"])
        assert set(got)==set(tc["output"]), tc["n"]