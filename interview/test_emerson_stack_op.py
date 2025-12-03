# Emerson online coding assessment
# Topic: Stack

# Given a list of stack operations, another stack operation and an value at the top of the stack. 
# You have to tell where the extra operation should go in the list of stack operations to get the given stack top value. 
from typing import List

def getOpIndex(ops: List[str], op: str, top: int) -> int:
    st = []

    i = 0
    while i<len(ops)+1:
        temp = ops.copy()
        temp.insert(i, op)

        for oper in temp:
            if "PUSH" in oper:
                st.append(int(oper.split()[1]))
            if "POP" in oper:
                if len(st)==0:
                    break
                st.pop()

        if len(st)>0:
            if top==st[-1]:
                return i
        st.clear()
        i+=1
    return -1

def test_getOpIndex():
    test_cases = [
        {
            "ops": ["PUSH 1", "PUSH 2", "POP", "PUSH 4"],
            "op": "POP",
            "top": 1,
            "output": 4,
        }, 
        {
            "ops": ["PUSH 1", "PUSH 2", "POP", "PUSH 4"],
            "op": "PUSH 5",
            "top": 5,
            "output": 4,
        }, 
        {
            "ops": ["PUSH 1", "PUSH 2", "PUSH 5", "POP"],
            "op": "PUSH 3",
            "top": 2,
            "output": 0,
        }, 
    ]

    for tc in test_cases:
        got = getOpIndex(tc["ops"], tc["op"], tc["top"])
        assert got==tc["output"], f"Ops={tc["ops"]}, Op={tc["op"]}, Top={tc["top"]}"