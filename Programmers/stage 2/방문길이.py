def solution(dirs):
    dic = {}
    cnt = 0
    x = 0
    y = 0
    for i in dirs :
        now_x = x
        now_y = y
        if i == 'U' and y < 5 :
            y += 1
        elif i == 'D' and y > -5 :
            y -= 1
        elif i == 'R' and x < 5 :
            x += 1
        elif i == 'L' and x > -5 :
            x -= 1
        else :
            continue
        if ((now_x,now_y),(x, y)) in dic or ((x, y),(now_x,now_y)) in dic :
            continue
        else :
            dic[((now_x,now_y),(x, y))] = True
            dic[((x, y),(now_x,now_y))] = True
        cnt += 1
    return cnt
