# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

def solution(A):
    result = (A[0] + A[1])/2.0   # The mininal average
    StartingP = 0     # The begin position of the first
                        # slice with mininal average
    for i in range(0, len(A)-2):
        # Try the next 2-element slice
        SumA=A[i] + A[i+1]
        if (SumA / 2) < result:
            result = (SumA / 2)
            StartingP = i
        # Try the next 3-element slice
        SumA +=A[i+2]
        if (SumA / 3) < result:
            result = (SumA / 3)
            StartingP = i
    # Try the last 2-element slice
    if (A[-1]+A[-2])/2.0 < result:
        result = (A[-1]+A[-2])/2.0
        StartingP = len(A)-2
    return StartingP


#Testing
TempA=[[1,2],[4,2,2,5,1,5,8]]
for i in TempA:
    A=i
    print('A = ', A ,'\t\tResult =', solution(A),'\n')
