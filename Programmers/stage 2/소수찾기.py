from itertools import permutations


def chk(j):
    for i in range(2, (j // 2) + 1):
        if j % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    s = set()
    for i in range(1, len(numbers) + 1):
        p = list(permutations(numbers, i))
        for j in p:
            tmp = int(''.join(j))
            s.add(tmp)

    for i in s:
        if not i in [1, 0] and chk(i):
            answer += 1

    return answer