def solution(s):
    s = list(s)
    stack = []
    while s :
        if not stack or stack[-1] != s[-1] :
            stack.append(s.pop())
        else :
            stack.pop()
            s.pop()
    return 1 if not stack else 0