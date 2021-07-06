def solution(A,B):
    A.sort(); B.sort(reverse=True)
    l = [A[i]*B[i] for i in range(len(A))]
    return sum(l)