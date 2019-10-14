# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N, A):
    TempMax=0              
    Counter =[TempMax]*N 
    MainMax=0             
    m=len(A)
    for i in range(m):        
        K=A[i]     
        if K==(N+1):
            MainMax = TempMax            
        else:
            if MainMax > Counter[K-1]:               
                Counter[K-1] = MainMax
            Counter[K-1] += 1
            
            if Counter[K-1]>TempMax:
                TempMax=Counter[K-1]
        
    for i in range(N):
        if Counter[i]<MainMax:
            Counter[i]=MainMax        
    return Counter

# Testing
tempA=[[3,4,4,6,1,4,4],[1],[1],[2],[2],[7],[7],[7]]
tempN=[5,3,2,2,3,6,7,8]
for i in range(len(tempN)):
    N=tempN[i]    
    A=tempA[i]    
    print('A = ', A,'\t\tN = ', N, '\t\tResult =', solution(N,A),'\n')
