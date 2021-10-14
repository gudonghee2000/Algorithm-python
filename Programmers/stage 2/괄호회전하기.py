def check(t) :
    i = 0
    stack = []
    stack.append(t[i])
    i += 1
    while i < len(t) :
        m = t[i]
        i += 1
        if not stack or m in ["(", "{", "["] :
            stack.append(m)
        elif stack :
            if m == ')' and stack[-1] == '(' :
                stack.pop()
            elif m == '}' and stack[-1] == '{' :
                stack.pop()
            elif m == ']' and stack[-1] == '[' :
                stack.pop()
    return True if not stack else False

def solution(s):
    cnt = 0
    t = s
    for i in range(len(s)) :
        if(check(t)) :
            cnt += 1
        t = t[1:len(t)] + t[0]
    return cnt