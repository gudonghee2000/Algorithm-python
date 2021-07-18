cnt = 0
def dfs(numbers, target, pos, ret) :
    if pos == len(numbers) :
        if ret == target :
            global cnt
            cnt += 1
        return
    dfs(numbers, target, pos+1, ret + numbers[pos])
    dfs(numbers, target, pos+1, ret - numbers[pos])
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    global cnt
    return cnt
