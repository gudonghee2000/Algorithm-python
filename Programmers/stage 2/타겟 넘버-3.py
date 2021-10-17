def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, ret) :
        if idx == n :
            if ret == target :
                nonlocal answer
                answer += 1
            return
        else :
            dfs(idx+1, ret+numbers[idx])
            dfs(idx+1, ret-numbers[idx])
    dfs(0, 0)
    return answer