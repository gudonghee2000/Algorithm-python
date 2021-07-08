def solution(msg):
    answer = []
    dic = {}
    num = 27;
    cnt = 0
    for i in range(26):
        dic[chr(65 + i)] = i + 1

    while True:
        if msg in dic:
            break
        cnt += 1
        chk = True
        if msg[:cnt] not in dic:
            dic[msg[:cnt]] = num
            answer.append(dic[msg[:cnt - 1]])
            msg = msg[cnt - 1:]
            num += 1
            cnt = 0

    answer.append(dic[msg])
    return answer