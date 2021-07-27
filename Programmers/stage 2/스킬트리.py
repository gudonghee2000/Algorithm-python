def solution(skill, skill_trees):
    ret = 0
    for i in skill_trees :
        stack = []
        pos = 0
        chk = True
        for j in i :
            if j in skill :
                stack.append(j)
        for t in range(len(stack)) :
            if stack[t] != skill[t] :
                chk = False
                break
        if chk == True :
            ret += 1
    return ret
