def step2(p):
    u = '';
    v = ''
    for i in range(len(p)):
        if not u or u.count("(") != u.count(")"):
            u += p[i]
        else:
            v = p[i:]
            break
    return u, v


def step3(u):
    stack = []
    u = list(u)
    while u:
        tmp = u.pop(0)
        if not stack or tmp == '(':
            stack.append(tmp)
        else:
            stack.pop()
    return True if not stack else False


def step4_4(u):
    u = list(u)
    u = u[1:len(u) - 1]
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return ''.join(u)


def solution(p):
    if not p:
        return ""

    u, v = step2(p)

    if (step3(u)):
        return u + solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        tmp += step4_4(u)
        return tmp
