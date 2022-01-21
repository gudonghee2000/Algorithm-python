from collections import defaultdict


def makeTime(time):
    a, b = time.split(":")
    a = int(a)
    b = int(b)
    return a * 60 + b


def solution(fees, records):
    infos = defaultdict(list)
    answers = {}
    last_answer = []

    for r in records:
        a, b, c = r.split(" ")
        infos[b].append(makeTime(a))

    for k, v in infos.items():
        if len(v) % 2 == 1:
            infos[k].append(23 * 60 + 59)

    for k, v in infos.items():
        while v:
            inTime = v.pop(0)
            outTime = v.pop(0)
            if k in answers:
                answers[k] += outTime - inTime
            else:
                answers[k] = outTime - inTime

    numbers = sorted(answers.items())

    for n in numbers:
        tmp = n[1] - fees[0]
        tmp2 = fees[1]
        if tmp <= 0:
            last_answer.append(tmp2)
            continue
        if tmp % fees[2] == 0:
            tmp2 += (tmp // fees[2]) * fees[3]
        else:
            tmp2 += ((tmp // fees[2]) + 1) * fees[3]
        last_answer.append(tmp2)

    return last_answer
