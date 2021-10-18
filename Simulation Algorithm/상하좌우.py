"""
문제 :
    여행가 A는 N x N 크기의 정사각형 공간에 위치.
    이 공간은 1 x 1 크기의 정사각형으로 구성되어있음
    가장 왼쪽 위 좌표는 (1, 1)
    가장 오른쪽 아래 좌표는 (N, N)
    여행가 A는 상, 하, 좌, 우 방향으로 이동 가능하면 시작 좌표는 (1, 1)
    여행가 A가 이동할 계획서

    한 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있음
    각 방향으로 한 칸 이동 (L: 왼쪽, R: 오른쪽, U: 위, D: 아래)
    N x N 정사각형 공간을 벗어나는 움직임은 무시됨
"""

def answer(N, direct):
    startR = 0
    startC = 0

    while direct:
        d = direct.pop(0)
        nR, nC = startR, startC
        if d == 'R':
            nC += 1
        elif d == 'L':
            nC -= 1
        elif d == 'U':
            nR -= 1
        elif d == 'D':
            nR += 1
        if 0 <= nR < N and 0 <= nC < N:
            startR, startC = nR, nC
    return [nR + 1, nC + 1]