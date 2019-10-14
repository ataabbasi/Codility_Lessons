# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

def solution(A):
    A.sort()
    result =0
    starting = 0
    for i in A:    
        if result>0:
            if result<i:              # i.e result=1 [1,1,1,2,4] / [1,2,4]
                result +=1
                if result != i:
                    return result     
        if i==1:
            starting =1              # to know that there is at least 1
            result =1 
    if starting == 0:
        return 1
    else:
        return (A[-1]+1)             # if everything is in A and it should retrun max+1
    
# Testing
tempA=[[3,4,4,6,1,4,4],[1, 2, 3],[-1,-3],[-1,1,2,3]]
for i in range(len(tempA)):      
    A=tempA[i]    
    print('A = ', A, '\t\tResult =', solution(A),'\n')
