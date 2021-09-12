def checker(u):
    stack = []
    if u[0] == ')': return False

    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()

    return False if stack else True


def change(u):
    tmp = ''
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp


def solution(p):
    l = list(p)

    if not l:
        return ''

    u = []
    v = []

    for i in range(len(l)):
        u.append(l[i])
        if u.count('(') == u.count(')'):
            for j in range(i + 1, len(l)):
                v.append(l[j])
            break

    if checker(u):
        return ''.join(u) + solution(''.join(v))
    else:
        return '(' + solution(''.join(v)) + ')' + change(u)