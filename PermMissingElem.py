def solution(A):

    n = len(A)+1
    # sum of n Natural number
    result = n * (n + 1)//2

    return result - sum(A)
