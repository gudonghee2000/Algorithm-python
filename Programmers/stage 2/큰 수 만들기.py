def solution(n, k):
    stack = []
    for i in range(len(n)) :
        while stack and stack[-1] < n[i] and k > 0 :
            stack.pop()
            k -= 1
        stack.append(n[i])
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)
