def solution(spell):
    spell = list(spell)
    stack = []
    for s in spell :
        if not stack or stack[-1] != s :
            stack.append(s)
        else :
            while stack and stack[-1] == s :
                stack.pop()
    return 1 if not stack else 0