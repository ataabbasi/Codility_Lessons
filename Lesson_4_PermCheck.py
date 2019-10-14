# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    A.sort()
    N=len(A)
    for i in range(N):
        if A[i]!=i+1:
            return 0
    return 1
  
# Testing
tempA=[[1,2],[2,1],[1,2,3],[3,1],[1,3,2,4],[1,4,1,4,5]]
for i in range(len(tempA)):
    A=tempA[i]
    print('A = ',A, '\t\tResult =', solution(A))
