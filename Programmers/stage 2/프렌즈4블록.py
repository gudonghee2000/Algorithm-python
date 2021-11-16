from collections import deque


def chk(board, r, c, candi):
    base = board[r][c]
    if base == "-":
        return False
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    for i in range(3):
        if base != board[r + dx[i]][c + dy[i]] or board[r + dx[i]][c + dy[i]] == "-":
            return False
    candi[r][c] = True
    for i in range(3):
        candi[r + dx[i]][c + dy[i]] = True

    return True


def solution(m, n, board):
    answer = 0
    c = -1
    for i in range(m):
        board[i] = list(board[i])
    while c != 0:
        c = 0
        candi = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                chk(board, i, j, candi)
        for i in range(n):
            stack = deque()
            for j in range(m):
                if candi[j][i] == False:
                    stack.appendleft(board[j][i])
                else:
                    c += 1
            for j in range(len(stack), m):
                stack.append("-")
            for j in range(m):
                board[j][i] = stack.pop()
        answer += c

    return answer