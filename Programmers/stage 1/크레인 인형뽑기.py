def solution(board, moves):
    cnt = 0
    bucket = []
    for i in moves:
        move = i - 1
        b_l = len(bucket)
        for i in range(len(board)):
            if board[i][move] != 0:
                bucket.append(board[i][move])
                board[i][move] = 0
                break

        if len(bucket) > 1 and bucket[b_l - 1] == bucket[b_l - 2]:
            del bucket[b_l - 1]
            del bucket[b_l - 2]
            cnt += 2
    return cnt