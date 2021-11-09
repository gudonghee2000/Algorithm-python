def solution(triangle):
    dp = []
    for i in range(1, len(triangle)) :
        for j in range(i+1) :
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1 :
                triangle[i][j] += triangle[i-1][j-1]
            else :
                if triangle[i-1][j-1] >= triangle[i-1][j] :
                    triangle[i][j] += triangle[i-1][j-1]
                else :
                    triangle[i][j] += triangle[i-1][j]
    return max(triangle[-1])