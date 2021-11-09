from collections import defaultdict


def solution(tickets):
    dic = defaultdict(list)

    for ticket in tickets:
        dic[ticket[0]].append(ticket[1])
        dic[ticket[0]].sort()

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(dic[top].pop(0))

    return path[::-1]