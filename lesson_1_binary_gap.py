# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):    
    if N<5:
        return 0
    else:
        N=format(N, "b")      # change N to binary format       
        c=0                   # c= last index of '1'
        d=0                   # d= max number of zeros between two '1'
        for i in range(len(N)):
            if N[i]=='1':                
                temp=i-c-1         
                d=max(temp, d)    
                c=i 
        return d  
        
 # testing
 a=list(i for i in range(100))
 for N in a:
    print(solution(N), format(N, "b"))
