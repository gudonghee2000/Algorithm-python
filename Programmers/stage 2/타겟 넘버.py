count = 0
def dfs(numbers, cnt, ret,t) :
    if cnt+1 == len(numbers) :
        if ret == t :
            global count
            count +=1
        return
    dfs(numbers, cnt+1, ret+numbers[cnt+1],t)
    dfs(numbers, cnt+1, ret-numbers[cnt+1],t)

def solution(numbers, target) :
    dfs(numbers,0, numbers[0], target)
    dfs(numbers,0, -numbers[0], target)
    answer = count
    return answer
