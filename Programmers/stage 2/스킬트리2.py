def solution(skill, skill_trees):
    ret = 0
    for tree in skill_trees:
        s = list(skill)
        check = True
        for i in range(len(tree)):
            if tree[i] in s:
                if tree[i] != s[0]:
                    check = False
                    break
                else:
                    s.pop(0)
        if check == True:
            ret += 1

    return ret