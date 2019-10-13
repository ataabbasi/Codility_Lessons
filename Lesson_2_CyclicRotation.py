# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):    
    m=len(A)
    if m<2 or K==0:
        return A
    else:
        K%=m                 # suppose A= [3,7] and K=98
        B=A.copy()        
        for i in range(m):
            if (i+K)<m:
                A[i+K]=B[i]                
            else:
                A[i+K-m]=B[i]    
        return A
# Testing
A0=[]
A1=[1]
A2=[1,2]
A3=[1,2,3]
A4=[1,2,3,4]

K0=0
K1=1
K2=2
K3=3
K4=4
K5=5
K6=6
K7=7
K8=8

A=A4
K=K6
solution(A, K)
