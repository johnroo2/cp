from typing import List

def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    ptr = 0

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)
    }

    while ptr < len(tokens):
        if tokens[ptr] in operations:
            res = operations[tokens[ptr]](stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res)
        else: 
            stack.append(int(tokens[ptr]))
        ptr += 1

    return stack[0]
