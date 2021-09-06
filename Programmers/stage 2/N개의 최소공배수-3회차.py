def gcd(a, b):
    while (b != 0):
        tmp = a % b
        a = b
        b = tmp
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    n = arr[0]

    for i in range(1, len(arr)):
        n = lcm(n, arr[i])

    return n