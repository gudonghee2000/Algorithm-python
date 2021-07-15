def solution(s):
    stack = []
    for i in s :
        if i == '(' or not stack :
            stack.append(i)
        else :
            if stack[-1] == ')' :
                break
            stack.pop()

    return True if not stack else False
