# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):   
    number_of_P=0
    result=0
    for i in A:
        if result>1000000000:
            return -1
        if i == 0:
            number_of_P +=1
        else:
            result +=number_of_P
    return result

# Testing
tempA=[[0], [0,1], [0,0], [0,0,0], [0,0,1], [0,1,0], [0,1,1], [0,0,0,0], [0,0,0,1], [0,0,1,0], [0,1,0,0],
       [0,0,1,1], [0,1,0,1], [0,1,1,0], [0,1,1,1], [1], [1,1], [1,0], [1,0,0], [1,0,1], [1,1,0], [1,1,1], 
       [1,0,0,0], [1,0,0,1],  [1,0,1,0], [1,1,0,0], [1,0,1,1], [1,1,0,1], [1,1,1,0], [0,1,1,1]]
for i in range(len(tempA)):      
    A=tempA[i]    
    print('A = ', A, '\t\tResult =', solution(A),'\n')
