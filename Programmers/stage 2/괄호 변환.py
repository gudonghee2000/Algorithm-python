def divide(p) :
    a = 0
    b = 0
    for i in range(len(p)) :
        if p[i] == '(' :
            a += 1
        elif p[i] == ')' :
            b += 1
        if a == b :
            return p[:i+1], p[i+1:]

def chk(u) :
    stack = []
    for i in u :
        if i == '(' :
            stack.append(i)
        else :
            if not stack :
                return False
            stack.pop()
    return True

def solution(p):
    if p == '' :
        return p
    u,v = divide(p)
    if chk(u) == True :
        return u + solution(v)
    else :
        newU = ''
        for i in range(1,len(u)-1) :
            if u[i] == '(' :
                newU += ')'
            else :
                newU += '('
        return '(' +solution(v) + ')' + newU