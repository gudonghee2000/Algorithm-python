def solution(n):
    jump = [1, 2]
    if n < 3:
        return jump[n - 1]
    for i in range(2, n):
        jump.append(jump[i - 2] + jump[i - 1])

    return jump[n - 1] % 1234567