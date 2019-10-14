# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    N=len(A)
    B=[1]*X    
    uncovered=X
    for i in range(N):
        temp=A[i] 
        if (temp-1)<X:
            if B[temp-1]!=0:
                B[temp-1]=0
                uncovered-=1
        if uncovered==0:
            return i
    return -1
# Testing
tempA=[[1,3,1,4,2,3,5,4,7,4,6]]
tempX=list(i for i in range(1,8))
for i in range(len(tempX)):
    X=tempX[i]    
    A=tempA[0]    
    print('A = ', A,'\t\tX = ', X, '\t\tResult =', solution(X,A))
