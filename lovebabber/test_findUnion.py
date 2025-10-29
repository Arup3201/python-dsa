
def findUnion(a, b):
    # return list(set(a) | set(b))

    union = []
    freq = dict()
    for item in a:
        if not freq.get(item, None):
            union.append(item)
            freq[item] = 1
        else:
            freq[item]+=1
    for item in b:
        if not freq.get(item, None):
            union.append(item)
            freq[item] = 1
        else:
            freq[item]+=1

    return union

def test_findUnion():
    test_cases = [
        {
            "a": [1, 2, 3, 2, 1], 
            "b": [3, 2, 2, 3, 3, 2], 
            "output": [1, 2, 3]
        }
    ]

    for tc in test_cases:
        got = findUnion(tc["a"], tc["b"])
        assert got==tc["output"], f"a={tc["a"]}, b={tc["b"]}"