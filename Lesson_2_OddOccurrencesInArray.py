# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    if len(A)==1:
        return A[0]
    else:
        A.sort()
        for i in range(0,(len(A)-1),2):
            if A[i]!=A[i+1]: 
                return A[i] 
        return A[-1]                     # if aswer is the largest number (last element of array)
# accuracy test
A=[6]
A=[5,3,6,5,6]
A=[5,3,3,6,6]
solution(A)

#speed test
A=list(-i for i in range(1000000))
A.sort()
