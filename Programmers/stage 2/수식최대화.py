from itertools import permutations


def calculator(expression, e, i):
    if i > 2:
        return
    if e[i] == "*":
        ret = 1
        tmp = expression.split("*")
        print(tmp)
        for j in range(len(tmp)):
            if tmp[j].isdigit() == False:
                tmp[j] = calculator(tmp[j], e, i + 1)
        for t in tmp:
            ret *= int(t)
        return str(ret)
    if e[i] == "+":
        tmp = expression.split("+")
        print(tmp)
        ret = 0
        for j in range(len(tmp)):
            if tmp[j].isdigit() == False:
                tmp[j] = calculator(tmp[j], e, i + 1)
        for t in tmp:
            ret += int(t)
        return str(ret)
    if e[i] == "-":
        tmp = expression.split("-")
        for j in range(len(tmp)):
            if tmp[j].isdigit() == False:
                tmp[j] = calculator(tmp[j], e, i + 1)
        print(tmp)
        ret = int(tmp[0])
        for j in range(1, len(tmp)):
            ret -= int(tmp[j])
        return str(ret)


def solution(expression):
    exp = list(permutations(["-", "+", "*"]))
    answer = 0
    for e in exp:
        tmp = abs(int(calculator(expression, e, 0)))
        if tmp > answer:
            answer = tmp
    return answer