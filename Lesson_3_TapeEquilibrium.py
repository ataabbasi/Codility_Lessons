# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    m=len(A)
    result=[0]*(m-1)          # faster than append
    a=0
    b=sum(A)
    for P in range(m-1):
        a+=A[P]
        b-=A[P]
        result[P]=abs(a-b) 
    return min(result)

# testing
tempA=[[1,2],[2,1],[1,1,1],[-1,1],[1,3,5,7],[-2,-4,5,7,9]]
for i in range(len(tempA)):
    A=tempA[i]
    print('A = ',A, '\t\tResult =', solution(A))
