from collections import defaultdict

def dfs(start, visit, graph):
    global cnt
    cnt += 1
    visit.append(start)
    for node in graph[start]:
        if node not in visit:
            dfs(node, visit, graph)


def solution(n, wires):
    global cnt
    answer = -1
    graph = defaultdict(list)
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    for w in wires:
        graph[w[0]].remove(w[1])
        graph[w[1]].remove(w[0])
        cnt = 0
        dfs(1, [], graph)
        second_tree = n - cnt
        if answer == -1 or answer > abs(cnt - second_tree):
            answer = abs(cnt - second_tree)
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    return answer