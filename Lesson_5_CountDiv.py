# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

def solution(A, B, K):
    if A==B:                         # fast check
        if A%K==0:
            return 1
        else:
            return 0
    if A>0 and K>B:                  # no need to check
        return 0
    for i in range(A,B+1):
        if i%K==0:                   # find first number example1 A=13 B=15 K=6  example2 A=13 B=15 K=7
            return (((B-i)//K)+1)
    return 0                         # example: A=13 B=15 K=6

# Testing
Test_Set = [[0,0,1,1],[0,0,2,1],[0,0,10,1],[0,0,100000000,1],[0,1,1,2],[0,2,1,3],[0,1000,1,1001],[0,1,2,1],
            [0,2,2,2],[0,2,3,1],[0,2,4,1],[3,17,2,7],[3,17,3,5],[3,17,4,4],[3,17,5,3],[3,17,6,2],[3,17,10,1],
            [13,15,6,0],[3,17,1000000000,0]]
for i in range(len(Test_Set)):
    A=Test_Set[i][0]
    B=Test_Set[i][1]
    K=Test_Set[i][2]
    Result= Test_Set[i][3]
    print('A = % 10d, B = % 10d, K = % 10d, Result = % 10.5f' %(A, B, K, Result-solution(A, B, K)))
