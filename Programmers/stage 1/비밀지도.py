def makeboard(arr1, n):
    board = []
    for a in arr1:
        tmp = ''
        while a:
            b = a % 2
            a = a // 2
            tmp += str(b)
        while len(tmp) < n:
            tmp += '0'
        board.append(tmp[::-1])
    return board


def solution(n, arr1, arr2):
    answer = []
    board1 = makeboard(arr1, n)
    board2 = makeboard(arr2, n)

    for b in zip(board1, board2):
        tmp = ''
        print(b)
        for i in range(len(b[0])):
            if b[0][i] == '0' and b[1][i] == '0':
                tmp += '0'
            else:
                tmp += '1'
        answer.append(tmp)
    for a in range(len(answer)):
        answer[a] = answer[a].replace('1', '#').replace('0', ' ')
    return answer