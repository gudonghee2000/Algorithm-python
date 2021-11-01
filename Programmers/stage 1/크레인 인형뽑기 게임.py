def solution(board, moves):
    cnt = 0
    bucket = []
    for move in moves:
        tmp = -1
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                tmp = board[i][move - 1]
                board[i][move - 1] = 0
                break
        if tmp != -1 and bucket and bucket[-1] == tmp:
            bucket.pop(-1)
            cnt += 2
        elif tmp != -1:
            bucket.append(tmp)

    return cnt