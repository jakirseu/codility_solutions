def solution(A):
    s = set()
    for item in A:
        s.add(item) if item not in s else s.remove(item)
    return s.pop()
