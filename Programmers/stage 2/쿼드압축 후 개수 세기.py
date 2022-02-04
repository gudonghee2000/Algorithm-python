import numpy as np

zero = 0
one = 0


def dfs(arr, length):
    global one
    global zero

    if length == 1:
        if arr[0][0] == 0:
            zero += 1
        else:
            one += 1
        return

    arr = np.array(arr)
    length = length // 2
    checker = True

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[0][0] != arr[i][j]:
                checker = False
                break

    if checker == True:
        if arr.size > 0:
            if arr[0][0] == 0:
                zero += 1
            else:
                one += 1

    else:
        dfs(arr[0:length, 0:length], length)
        dfs(arr[0:length, length:length * 2], length)
        dfs(arr[length:length * 2, 0:length], length)
        dfs(arr[length:length * 2, length:length * 2], length)


def solution(arr):
    a = len(arr)
    arr = np.array(arr)
    dfs(arr, a)

    return [zero, one]