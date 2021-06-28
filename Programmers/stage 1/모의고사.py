def solution(answers):
    count = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ret = []
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            count[0] += 1
        if answers[i] == second[i % 8]:
            count[1] += 1
        if answers[i] == third[i % 10]:
            count[2] += 1

    chk = max(count)

    for i in range(len(count)):
        if chk == count[i]:
            ret.append(i + 1)
    return ret
