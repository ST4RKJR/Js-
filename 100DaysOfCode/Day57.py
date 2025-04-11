def removeOuterParentheses(S):
    stack = []
    result = []
    start = 0 

    for i, ch in enumerate(S):
        if ch == '(':
            stack.append(ch)
        else:
            stack.pop()
            if not stack:
                result.append(S[start + 1:i])
                start = i + 1

    return "".join(result)

S = input()
print(removeOuterParentheses(S))
