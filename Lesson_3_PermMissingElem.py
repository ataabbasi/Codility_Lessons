# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):    
    A.sort()
    for i in range(len(A)):
        if A[i]!=(i+1):
            return i+1        
    return (len(A)+1)           # if last number is missing (N+1)
   
# testing    
temp1=[[],[1],[2],[1,2],[2,1],[1,2,4],[2,1,4],[4,2,3],[2,3,1,5]]
for i in range(len(temp1)):
    A=temp1[i]
    print('A = ',A, '\t\tN = ', len(A),'\t\tResult =', solution(A))
