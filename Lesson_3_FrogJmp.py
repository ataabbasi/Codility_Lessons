# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    if X==Y:
        return 0
    elif (Y-X)%D ==0:
        return (Y-X)//D
    else:
        return ((Y-X)//D + 1)
#testing
X = 10

Y1=10
Y2=11
Y3=40
Y4=41

D1=1
D2=30
D3=10000

Y = Y4
D = D3
solution(X, Y, D)
