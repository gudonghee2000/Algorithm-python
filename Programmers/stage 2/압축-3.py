def solution(msg):
    answer = []
    msg = list(msg)
    word = ""
    dic = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alpha)) :
        dic[alpha[i]] = i+1
    while msg :
        tmp = msg.pop(0)
        if word + tmp not in dic :
            answer.append(dic[word])
            dic[word+tmp] = len(dic) + 1
            word = ""
        word += tmp
    if word != '' :
        answer.append(dic[word])
    return answer