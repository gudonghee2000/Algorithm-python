def solution(priorities, location):
    if len(priorities) == 1:
        return 1
    pos = [i for i in range(len(priorities))]
    cnt = 0

    while location in pos:
        a = priorities.pop(0)
        b = pos.pop(0)
        if not pos:
            break
        if a >= max(priorities):
            cnt += 1
        else:
            priorities.append(a)
            pos.append(b)
    return cnt if pos else cnt + 1