def solution(n):
    answer = ''
    while n > 0:
        tmp = n % 3
        if tmp == 0:
            answer += '4'
            n = n // 3 - 1
        else:
            answer += str(tmp)
            n = n // 3

    return answer[::-1]
