import sys
sys.setrecursionlimit(10 ** 7)

def fib(n, dic):
    if n in dic:
        return dic[n]
    else:
        dic[n] = fib(n - 1, dic) + fib(n - 2, dic)
        return dic[n]

def solution(n):
    dic = {0: 0, 1: 1}
    t = fib(n, dic)
    return t % 1234567