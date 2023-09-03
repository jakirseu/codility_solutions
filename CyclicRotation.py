def solution(A, K):

  # check is list empty. 
  # Otherwise you will not get 100% score. 
    if len(A) == 0:
        return A
    while K > 0:
      # poping last item and adding to first position of the list. 
        A.insert(0, A.pop(-1))
        K -= 1
    return A
