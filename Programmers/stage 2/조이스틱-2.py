def solution(name):
    name = list(name)
    if name.count('A') == len(name) :
        return 0
    target = ['A' for _ in range(len(name))]
    cnt = 0
    now_pos = 0
    while target != name :
        s, r = 0, 0
        if ord(name[now_pos]) - ord(target[now_pos]) <=13 :
            cnt += ord(name[now_pos]) - ord(target[now_pos])
        else :
            cnt += 26 - (ord(name[now_pos]) - ord(target[now_pos]))
        target[now_pos] = name[now_pos]
        if target == name :
            break
        for i in range(now_pos+1, now_pos+len(name)) :
            i = i%len(name)
            s += 1
            if name[i] != 'A' and target[i] != name[i] :
                break

        for i in range(now_pos+len(name)-1, now_pos, -1) :
            i = i%len(name)
            r += 1
            if name[i] != 'A' and target[i] != name[i] :
                break
        if s > r :
            now_pos = -(-(now_pos-r))%len(name)
            cnt += r
        else :
            now_pos = (now_pos+s)%len(name)
            cnt += s
    return cnt