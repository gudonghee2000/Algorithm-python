def checker(number):
    if number == '':
        return False
    number = int(number)
    if number < 2:
        return False
    for i in range(3, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    new_number = 0
    cnt = 1
    while n > 0:
        tmp = n % k
        n = n // k
        new_number += tmp * cnt
        cnt *= 10

    new_number = list(str(new_number))
    tmp2 = ''

    while len(new_number) != 0:
        tmp3 = new_number.pop(0)
        if tmp3 != '0':
            tmp2 += tmp3
            print(tmp2)
        elif tmp3 == '0':
            if checker(tmp2):
                answer += 1
            else:
                tmp2 = ''
        if len(new_number) != 0 and new_number[0] == '0' and checker(tmp2):
            answer += 1
            tmp2 = ''
        elif len(new_number) == 0 and checker(tmp2):
            answer += 1

    return answer
