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


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        
        return "".join(res)