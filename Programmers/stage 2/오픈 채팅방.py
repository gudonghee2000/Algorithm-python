def solution(record):
    answer = []
    id = []
    dic = {}
    for i in record:
        a = i.split(' ')
        if a[0] == 'Enter':
            answer.append('님이 들어왔습니다.')
            dic[a[1]] = a[2]
            id.append(a[1])
        elif a[0] == 'Leave':
            answer.append('님이 나갔습니다.')
            id.append(a[1])
        elif a[0] == 'Change':
            dic[a[1]] = a[2]

    for i in range(len(answer)):
        answer[i] = dic[id[i]] + answer[i]

    return answer
