def solution(m, n, puddles):
    table = [[0 for _ in range(m)] for _ in range(n)]
    table[0][0] = 1
    route = [[True for _ in range(m)] for _ in range(n)]

    for p in puddles:
        if p[1] - 1 == 0:
            for i in range(p[0] - 1, len(table[p[1]])):
                route[p[1] - 1][i] = False
        elif p[0] - 1 == 0:
            for i in range(p[1] - 1, len(table)):
                route[i][p[0] - 1] = False
        else:
            route[p[1] - 1][p[0] - 1] = False

    for i in range(len(table)):
        for j in range(len(table[i])):
            if i == 0 and j == 0 or route[i][j] == False:
                continue
            elif i == 0:
                table[i][j] = table[i][j - 1]
            elif j == 0:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[n - 1][m - 1] % 1000000007